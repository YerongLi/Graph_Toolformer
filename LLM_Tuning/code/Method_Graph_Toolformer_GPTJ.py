'''
Concrete MethodModule class for a specific learning MethodModule
'''

# Copyright (c) 2017-Current Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD

from code.base_class.method import method
from code.Module_GPTJ_8bit import GPTJForCausalLM, add_adapters
from code.Evaluate_Metrics import Evaluate_Metrics

import time
from datetime import datetime

import torch
import torch.nn.functional as F

from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM
from bitsandbytes.optim import Adam8bit

class Method_Graph_Toolformer_GPTJ(method):
    data = None
    max_epoch = None
    learning_rate = 1e-5
    weight_decay = 1e-2
    max_length = 128
    fine_tuned_checkpoint_filename = None
    checkpoint_name = "EleutherAI/gpt-j-6b"
    model_checkpoint = "hivemind/gpt-j-6B-8bit"
    cache_dir = "./pretrained_model/gpt-j-6b-8bit"

    def __init__(self, mName="", mDescription="",  checkpoint_name=None, cache_dir=None, device='cuda', pad_token='<'):
        method.__init__(self, mName, mDescription)
        self.device = device
        self.checkpoint_name = checkpoint_name
        self.cache_dir = cache_dir
        print('loading config...')
        self.config = AutoConfig.from_pretrained(self.checkpoint_name, cache_dir=self.cache_dir)
        print('loading tokenizer...')
        self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint_name, cache_dir=self.cache_dir, bos_token='<|startoftext|>', eos_token='<|endoftext|>', pad_token=pad_token)
        print('loading pretrained_model...')
        self.model = GPTJForCausalLM.from_pretrained(self.model_checkpoint, low_cpu_mem_usage=True, cache_dir=self.cache_dir).to(self.device)
        # self.model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", revision="float16", torch_dtype=torch.float16, low_cpu_mem_usage=True).to(self.device)
        print('define 8bit optimizer...')
        self.optimizer = Adam8bit(self.model.parameters(), lr=self.learning_rate, weight_decay=self.weight_decay)

    def load_checkpoint(self, checkpoint_dir="./finetuned_checkpoints/graph_toolformer"):
        date_str = datetime.today().strftime('%Y-%m-%d')
        checkpoint = torch.load(checkpoint_dir+"_"+self.fine_tuned_checkpoint_filename+"_"+date_str, map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

    def save_checkpoint(self, checkpoint_dir="./finetuned_checkpoints/graph_toolformer"):
        date_str = datetime.today().strftime('%Y-%m-%d')
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict()
        }, checkpoint_dir+"_"+self.fine_tuned_checkpoint_filename+"_"+date_str)

    def train_model(self, train_dataloader=None):
        self.model.gradient_checkpointing_enable()
        t_begin = time.time()
        for epoch in range(self.max_epoch):
            count = 0

            for ii, batch in enumerate(train_dataloader):
                # print('*********************** batchshape *************')
                # print(len(batch['full']))
                str_inputs = [batch['full'][i] for i in range(len(batch['full']))]
                # print('str_inputs[0]')
                # print(str_inputs[0])
                # Input: The chemical molecular graph instance #275 in the ptc dataset has a function of [TBR]. Output: The chemical molecular graph [33/1922]#275 in the ptc dataset has a function of [GR(GL("ptc"), "seg_bert:molecule_function", instance#275)-->r].
                # str_inputs[0]
                # Input: The citeseer bibliographic network' paper #2489 is concerned with the area of [TBR]. Output: The citeseer bibliographic network' pap$e #2489 is concerned with the area of [GR(GL("citeseer"), "graph_bert:topic", paper#2489)-->r].
                # str_inputs[0]
                # Input: How likely user #u1388 will be interested in music of artisit #i15237 in Last-fm? Output: The likelihood that user #u1388 will be in$trested in music from artisit #i15237 in Last-fm is [GR(GL("last-fm"), "bpr:recommendation", user#u1388, artisit#i15237)-->r].
                # str_inputs[0]
                # Input: The function for the protein molecular graph identified as #747 in proteins is [TBR]. Output: The function for the protein molecular graph identified as #747 in proteins is [GR(GL("proteins"), "seg_bert:molecule_function", instance#747)-->r].
                # str_inputs[0]
                # Input: According to the WorldNet knowledge graph, via relation #_hyponym, what entity can we obtain from entity #bat_mitzvah.n.01? Output: $Acording to the WorldNet knowledge graph, via relation #_hyponym, we can obtain entity #bat_mitzvah.n.01 from entity [GR(GL("worldnet"), "t$rnse:head_entity", relation#_hyponym, entity#bat_mitzvah.n.01)-->r].
                # str_inputs[0]
                # Input: According to the WorldNet knowledge graph, from entity #united_states.n.01, via relation #_has_part, we can derive entity #[TBR]. Ou$tut: According to the WorldNet knowledge graph, from entity #united_states.n.01, via relation #_has_part, we can derive entity [GR(GL("worl$det"), "transe:tail_entity", entity#united_states.n.01, relation#_has_part)-->r].
                # str_inputs[0]
                # Input: The chemical molecular graph instance #3423 in the nci1 dataset has a function of [TBR]. Output: The chemical molecular graph instance #3423 in the nci1 dataset has a function of [GR(GL("nci1"), "seg_bert:molecule_function", instance#3423)-->r].
                str_labels = [batch['full'][i] for i in range(len(batch['full']))]
                inputs = self.tokenizer(str_inputs, padding='max_length', max_length=self.max_length, truncation=True)
                labels = self.tokenizer(str_labels, padding='max_length', max_length=self.max_length, truncation=True)
                inputs = torch.LongTensor(inputs["input_ids"]).to(self.device)
                labels = torch.LongTensor(labels["input_ids"]).to(self.device)

                with torch.cuda.amp.autocast():
                    outputs = self.model.forward(inputs)
                    loss = F.cross_entropy(outputs.logits[:, :-1, :].flatten(0, -2), labels[:, 1:].flatten(), reduction='mean')

                if count % 10 == 0:
                    print('epoch: {}/{}'.format(epoch, self.max_epoch), 'batch: {}/{}'.format(count, len(train_dataloader)), 'loss: {}'.format(loss),  'time elapsed: {:.4f}s'.format(time.time()-t_begin))
                count += 1

                loss.backward()
                self.optimizer.step()
                self.optimizer.zero_grad()
                if ii > 10:
                    break
            if False:
                self.test(self.data['test'], fast_check=True)
        self.model.gradient_checkpointing_disable()


    def test(self, test_dataloader=None, fast_check=False):
        t_begin = time.time()
        true_result = []
        pred_result = []
        reason_result = []
        count = 0

        for ii, batch in enumerate(test_dataloader):
            for index in range(len(batch['inputs'])):
                payload = batch['inputs'][index] + ' Output: '
                reasoning_output = batch['local_data'][index]
                generated_outputs = self.inference(input_text=payload)
                true_result.append(batch['full'][index])
                pred_result.append(generated_outputs[0])
                reason_result.append(reasoning_output)
            if count % 1 == 0:
                print('batch: {}/{}'.format(count, len(test_dataloader)), 'time elapsed: {:.4f}s'.format(time.time() - t_begin))
            count += 1
            if fast_check:
                break
            if ii > 3:
                break

        result = {'pred': pred_result, 'true': true_result, 'local_data': reason_result}
        if fast_check:
            eval_obj = evaluate_obj = Evaluate_Metrics('metrics', '')
            eval_obj.data = result
            print(result)
            print(evaluate_obj.evaluate())
        return result

    def inference(self, input_text=''):
        if input_text is None or input_text == '':
            payload = self.tokenizer.bos_token2
        else:
            payload = input_text
        inputs = self.tokenizer(text=payload, return_tensors="pt")
        inputs = inputs.to(self.device)
        sample_outputs = self.model.generate(
            inputs["input_ids"],
            num_beams=5, top_k=5, top_p=0.95, temperature=1.9,
            bos_token_id=self.tokenizer.bos_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.eos_token_id,
            num_return_sequences=1, max_length=self.max_length,
            #max_new_tokens=self.max_length, do_sample=False,
        )
        output_str = [self.tokenizer.decode(sample_output, skip_special_tokens=True) for i, sample_output in enumerate(sample_outputs)]
        return output_str
    
    def run(self):
        print('method running@{}...'.format(self.device))
        train_tag = True
        result = None

        if train_tag:

            print('--start training...')
            self.train_model(train_dataloader=self.data['train'])

            print('--saving checkpoint...')
            self.save_checkpoint()

            print('--start testing...')
            result = self.test(test_dataloader=self.data['test'], fast_check=False)
        else:
            print('--loading checkpoint...')
            self.load_checkpoint()

            print('--start testing...')
            result = self.test(test_dataloader=self.data['test'], fast_check=False)

        return result



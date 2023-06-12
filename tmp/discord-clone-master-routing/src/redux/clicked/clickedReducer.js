const initialState={
    clicked:false,
  }
   const replyopenReducer=(state=initialState,action)=>{
    switch(action.type){
      case 'Clicked':
      return {
        ...state,
        clicked:!state.clicked,
      }
      default: return state
    }
  }
  export default replyopenReducer
  
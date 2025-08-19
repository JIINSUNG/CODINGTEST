function solution(s)
{
  const stack = [];

  for (const alpha of s) {
    if (stack.length > 0 && stack[stack.length - 1] === alpha) {
      stack.pop(); 
    } else {
      stack.push(alpha);
    }
  }

   if(stack.length === 0){
       return 1 
   }
    return 0
    
}
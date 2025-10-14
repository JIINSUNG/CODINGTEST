function solution(arr1, arr2) {
    var answer = 0;
    
    if(arr1.length > arr2.length){
        return 1
    }else if (arr1.length < arr2.length){
        return -1
    }else {
        if (arr1.reduce((acc, val) => acc + val) > (arr2.reduce((acc, val) => acc + val))){
            return 1
        }else if (arr1.reduce((acc, val) => acc + val) < arr2.reduce((acc, val) => acc + val)){
            return -1
        }else {
            return 0 
        }
    }
}

var twoSum = function(nums, target){
	var outputArray = [];
	for(var i = 0; i <= nums.length; i++){
		for(var j = 0; j <= nums.length; j++){
			if(nums[i] + nums[j] == target){
				if(!(outputArray.includes(i)) && (i != j)){
					console.log(i);
					outputArray.push(i);
					}
				}
			}
		}
		return outputArray;
};


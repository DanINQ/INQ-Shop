'use strict';

var rangeInput = document.querySelectorAll(".range-input input"),
numberInput = document.querySelectorAll(".field input"),
progress = document.querySelector(".slider .progress");

let priceGap = 1000;

rangeInput.forEach(input => {
	input.addEventListener("input", (e) => {
		let minVal = parseInt(rangeInput[0].value),
		maxVal = parseInt(rangeInput[1].value);

		if(maxVal - minVal < priceGap){
			if(e.target.className === "range-min"){
				rangeInput[0].value = maxVal - priceGap;
			}else{
				rangeInput[1].value = minVal + priceGap;
			}
		}else{
			numberInput[0].value = minVal;
			numberInput[1].value = maxVal;
			progress.style.left = (minVal / rangeInput[0].max) * 100 + "%";
			progress.style.right = 100 - ((maxVal / rangeInput[0].max) * 100) + "%";
		}
	})
})


numberInput.forEach(input => {
	input.addEventListener("input", (e) => {
		let minVal = parseInt(numberInput[0].value),
		maxVal = parseInt(numberInput[1].value);
		if((maxVal - minVal >= priceGap) && (maxVal <= 10000) && (minVal >= 0)){
			if(e.target.className === "input-min"){
				rangeInput[0].value = minVal;
				progress.style.left = (minVal / rangeInput[0].max) * 100 + "%";
			}else{
				rangeInput[1].value = maxVal;
				progress.style.right = 100 - ((maxVal / rangeInput[1].max) * 100) + "%";
			}
		}
	})
})

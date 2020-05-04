window.addEventListener('DOMContentLoaded', () => {
	let balanceNode = document.querySelector('#balance')
	let balanceValue = Number(balanceNode.getAttribute('value'))

	if (balanceValue < 0) balanceNode.classList.add('text-danger')
	if (balanceValue == 0) balanceNode.classList.add('text-warning')
	if (balanceValue > 0) balanceNode.classList.add('text-success')
	balanceNode.innerText = balanceValue + ' zł'
})
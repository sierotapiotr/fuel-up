<template>
	<div class="row fixed-bottom bg-dark text-light">
		<div class="col-6">
			<router-link to="/refuel" class="d-block py-4 my-2 text-center align-middle text-light">
				<i class="fas fa-gas-pump fa-3x"></i>
				<p class="mt-2">Tankowanie</p>
			</router-link>
		</div>
		<div class="col-6">
			<router-link to="/trips" class="d-block py-4 my-2 text-center align-middle text-light">
				<i class="fas fa-car fa-3x"></i>
				<p class="mt-2">Przejazd</p>
			</router-link>
		</div>
	</div>
</template>

<script>
	export default {
		name: "NavButtons"
	}
</script>

<style scoped>

</style>

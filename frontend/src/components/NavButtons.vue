<template>
	<div class="row fixed-bottom bg-dark text-light">
		<div class="col-6">
			<div class="d-block py-4 my-2 text-center">
				<router-link to="/refuel" class="align-middle text-light h1">
					<i class="fas fa-gas-pump"></i>
				</router-link>
				<p>Tankowanie</p>
			</div>
		</div>
		<div class="col-6">
			<div class="d-block py-4 my-2 text-center">
				<router-link to="/trips" class="align-middle text-light h1">
					<i class="fas fa-car"></i>
				</router-link>
				<p>Przejazd</p>
			</div>
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

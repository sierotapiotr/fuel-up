<template>
	<div class="container">
		<div class="row">
			<div class="col-12">
				<p id="balance" value="0" class="display-3 text-center pt-5 mb-0">B/D</p>
				<p class="text-center text-secondary pb-5 mb-0">twój bilans</p>
			</div>
		</div>
		<div class="row">
			<div class="col-12">
				<table class="table table-hover text-center table-sm">
					<thead>
					<tr>
						<th scope="col"><i class="fas fa-car"></i></th>
						<th scope="col"><i class="fas fa-road"></i></th>
						<th scope="col"><i class="fas fa-coins"></i></th>
					</tr>
					</thead>
					<tbody>
					<tr>
						<td>{car}</td>
						<td>{carDistance}</td>
						<td>{carCosts}</td>
					</tr>
					</tbody>
				</table>
			</div>
		</div>
		<div class="row fixed-bottom bg-dark text-light">
			<div class="col-6">
				<div class="d-block py-4 my-2 text-center">
					<a href="refuel" class="align-middle text-light h1">
						<i class="fas fa-gas-pump"></i>
					</a>
					<p>Tankowanie</p>
				</div>
			</div>
			<div class="col-6">
				<div class="d-block py-4 my-2 text-center">
					<a href="trip" class="align-middle text-light h1">
						<i class="fas fa-car"></i>
					</a>
					<p>Przejazd</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: "Home"
	}
</script>

<style scoped>

</style>

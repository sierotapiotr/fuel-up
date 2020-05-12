<template>
	<div>
		<Navbar/>
		<div class="container">
			<form novalidate>
				<div class="form-group">
					<div class="d-flex justify-content-between">
						<label>Podróżujący:</label>
						<div class="custom-control custom-checkbox">
							<input type="checkbox" class="custom-control-input" id="selectAll">
							<label class="custom-control-label" for="selectAll">Wszyscy</label>
						</div>
					</div>
					<div class="custom-control custom-checkbox">
						<input type="checkbox" class="custom-control-input" id="select1" name="persons" value="tomasz">
						<label class="custom-control-label" for="select1">Tomasz</label>
					</div>
					<div class="custom-control custom-checkbox">
						<input type="checkbox" class="custom-control-input" id="select2" name="persons" value="damian">
						<label class="custom-control-label" for="select2">Damian</label>
					</div>
					<div class="custom-control custom-checkbox">
						<input type="checkbox" class="custom-control-input" id="select3" name="persons" value="pawel">
						<label class="custom-control-label" for="select3">Paweł</label>
					</div>
					<div class="custom-control custom-checkbox">
						<input type="checkbox" class="custom-control-input" id="select4" name="persons" value="wiktor">
						<label class="custom-control-label" for="select4">Wiktor</label>
					</div>
					<div class="custom-control custom-checkbox">
						<input type="checkbox" class="custom-control-input" id="select5" name="persons" value="piotr">
						<label class="custom-control-label" for="select5">Piotr</label>
					</div>
					<div class="custom-control custom-checkbox">
						<input type="checkbox" class="custom-control-input" id="select6" name="persons" value="jacek">
						<label class="custom-control-label" for="select6">Jacek</label>
					</div>
				</div>
				<div class="form-group">
					<label>Dystans:</label>
					<input type="number" class="form-control" placeholder="(km)" name="distance">
				</div>
				<div class="form-group">
					<label>Pojazd:</label>
					<select class="form-control" name="vehicle" required>
						<option value="" disabled selected>wybierz...</option>
						<option value="toyota">Toyota</option>
						<option value="peugeot">Peugeot</option>
					</select>
				</div>
				<button type="submit" class="btn btn-secondary w-100 fixed-bottom rounded-0">Zapisz</button>
			</form>
		</div>
	</div>
</template>

<script>
	import Navbar from "../components/Navbar";

	export default {
		name: "Ride",
		components: { Navbar }
	}
</script>

<style scoped>

</style>

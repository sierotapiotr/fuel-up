<template>
	<div>
		<Navbar />
		<div class="container">
			<form>
				<div class="form-group">
					<label for="refuelUser">Odbiorca zwrotu</label>
					<select name="refuelUser" class="custom-select" id="refuelUser" required>
						<option selected disabled value="">Wybierz...</option>
						<option value="1">{user}</option>
					</select>
				</div>
				<div class="form-group">
					<label for="price">Kwota (zł)</label>
					<input name="price" type="number" id="price" class="form-control" required>
					<div class="invalid-feedback">
						Please choose a username.
					</div>
				</div>
				<button type="button" class="btn btn-secondary w-100 fixed-bottom rounded-0">Zapisz</button>
			</form>
		</div>
	</div>
</template>

<script>
	import Navbar from "../components/Navbar";
	export default {
		name: "Transaction",
		components: { Navbar }
	}
</script>

<style scoped>

</style>

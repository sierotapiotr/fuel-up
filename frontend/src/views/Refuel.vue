<template>
	<div>
		<Navbar/>
		<div class="container">
			<form novalidate>
				<div class="form-group">
					<label for="refuelUser">Osoba tankująca</label>
					<select name="refuelUser" class="custom-select" id="refuelUser" required>
						<option selected disabled value="">Wybierz...</option>
						<option value="1">{user}</option>
					</select>
				</div>
				<div class="form-group">
					<label for="vehicle">Pojazd</label>
					<select name="vehicle" class="custom-select" id="vehicle" required>
						<option selected disabled value="">Wybierz...</option>
						<option value="1">{car}</option>
					</select>
				</div>
				<p class="text-muted">Typ paliwa</p>
				<div class="btn-group btn-group-toggle w-100 mb-3" role="group" data-toggle="buttons" disabled>
					<label class="btn btn-outline-secondary w-50">
						<input type="radio" name="fuelType" id="1" disabled>Benzyna/Olej
					</label>
					<label class="btn btn-outline-secondary w-50">
						<input type="radio" name="fuelType" id="2" disabled>Gas
					</label>
				</div>
				<div class="form-group">
					<label for="amount">Ilość (l)</label>
					<input name="amount" type="number" id="amount" class="form-control">
				</div>
				<div class="form-group">
					<label for="price">Kwota (zł)</label>
					<input name="price" type="number" id="price" class="form-control" required>
					<div class="invalid-feedback">
						Please choose a username.
					</div>
				</div>
				<button type="submit" class="btn btn-secondary w-100 fixed-bottom rounded-0">Zapisz</button>
			</form>
		</div>
	</div>
</template>

<script>
	import Navbar from "../components/Navbar";

	export default {
		name: "Refuel",
		components: { Navbar },
	}
</script>

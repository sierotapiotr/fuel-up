<template>
	<nav class="navbar navbar-dark bg-dark">
		<router-link class="navbar-brand" to="/">{{ brand }}</router-link>
		<button class="btn btn-link" data-toggle="dropdown" role="button">
			<i class="fas fa-user-circle text-white"></i>
		</button>
		<div class="dropdown-menu dropdown-menu-right">
			<a href="#" class="btn dropdown-item" type="button">Settings</a>
			<router-link to="/transaction" class="btn dropdown-item" type="button">Transaction</router-link>
		</div>
	</nav>
</template>

<script>
	export default {
		name: "Navbar",
		data(){
			return {
				brand: "Fuel-up"
			}
		}
	}
</script>

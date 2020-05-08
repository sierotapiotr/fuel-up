<template>
	<div>
		<Navbar />
		<Home />
	</div>
</template>

<script>
	import Navbar from "./components/Navbar";
	import Home from "./components/Home";

	export default {
		name: 'Fuel-up',
		components: { Navbar, Home }
	}
</script>

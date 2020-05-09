<template>
	<div>
		<Navbar />
		<h1>Ups...</h1>
		<h5>Coś poszło nie tak...</h5>
	</div>
</template>

<script>
	import Navbar from "../components/Navbar";
	export default {
		name: "Error",
		components: { Navbar }
	}
</script>

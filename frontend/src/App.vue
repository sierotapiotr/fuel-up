<template>
	<div id="main">
		<Navbar/>
		<router-view></router-view>
	</div>
</template>

<script>
	import Navbar from "./components/Navbar";

	export default {
		name: 'Fuel-up',
		components: { Navbar }
	}
</script>

<style>
	#main {
		width: 100%;
		min-width: 100vw;
		height: 100%;
		min-height: 100vh;
	}
</style>

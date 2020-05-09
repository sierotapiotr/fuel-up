<template>
	<div>
		<Navbar />
		<Main />
		<NavButtons />
	</div>
</template>

<script>
	import Main from "../components/Main";
	import Navbar from "../components/Navbar";
	import NavButtons from "../components/NavButtons";
	export default {
		name: "Home",
		components: { NavButtons, Navbar, Main }
	}
</script>

<style scoped>

</style>

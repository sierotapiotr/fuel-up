<template>
	<div>
		<Main />
		<NavButtons />
	</div>
</template>

<script>
	import Main from "../components/Main";
	import NavButtons from "../components/NavButtons";
	export default {
		name: "Home",
		components: { NavButtons, Main }
	}
</script>

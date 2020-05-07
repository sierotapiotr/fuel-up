<template>
	<nav class="navbar navbar-dark bg-dark">
		<a class="navbar-brand" href="#">{{ brand }}</a>
	</nav>
</template>

<script>
    export default {
        name: "Navbar",
        data() {
            return {
                brand: "Fuel-up"
            }
        }
    }
</script>

<style scoped>

</style>

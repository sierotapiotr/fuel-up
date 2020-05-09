import Vue from 'vue'
import VueRouter from 'vue-router'
import Error from "../views/Error";
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},
	{
		path: '*',
		name: 'Error',
		component: Error
	}
]

const router = new VueRouter({ routes })

export default router

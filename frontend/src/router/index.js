import Vue from 'vue'
import VueRouter from 'vue-router'
import Error from "../views/Error";
import Home from '../views/Home.vue'
import Refuel from '../views/Refuel'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},
	{
		path: '/refuel',
		name: 'Refuel',
		component: Refuel
	},
	{
		path: '*',
		name: 'Error',
		component: Error
	}
]

const router = new VueRouter({ routes })

export default router

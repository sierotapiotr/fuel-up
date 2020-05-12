import Vue from 'vue'
import VueRouter from 'vue-router'
import Error from '../views/Error'
import Home from '../views/Home.vue'
import Refuel from '../views/Refuel'
import Ride from '../views/Ride'
import Transaction from '../views/Transaction'

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
		path: '/ride',
		name: 'Ride',
		component: Ride
	},
	{
		path: '/transaction',
		name: 'Transaction',
		component: Transaction
	},
	{
		path: '*',
		name: 'Error',
		component: Error
	}
]

const router = new VueRouter({ routes })

export default router

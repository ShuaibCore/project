import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
export default new Router({
mode: 'history',
base: '/',
routes:[
{
    path: '*',
    name:'404',
    meta:{layout: 'GeneralHeader', title:'404-page',},
    component: ()=> import('./views/PageNotFound.vue'),
},
{
    path: '/',
    name:'Home',
    meta:{layout:'GeneralHeader', title:'Home'},
    component: ()=> import('./views/Home.vue'),
},
{
    path: '/oath/logout',
    name: 'logout',
    meta: {layout:'BackendHeader', title: 'logout'},
    component: ()=> import('./secure/Logout.vue')
},
{
    path: '/site/about',
    name:'About',
    meta:{layout:'GeneralHeader', title:'About us',},
    component: ()=> import('./views/About.vue')
},
{
    path: '/site/contact',
    name:'Contact',
    meta:{layout:'GeneralHeader', title:'Contact us'},
    component: ()=> import('./views/Contactus.vue')
},
{
    path: '/oath/statement',
    name:'Statement',
    meta:{layout:'SidebarNoOath', title:'statement'},
    component: ()=> import('./views/About.vue')
},
{
    path: '/oath/signin',
    name:'Signin',
    meta:{layout:'GeneralHeader', title: 'Sign In'},
    component: ()=> import('./secure/Signin.vue')
},
{
    path: '/oath/dashboard',
    name: 'dashboard',
    meta: {layout:'SidebarNoOath', title: 'Dashboard'},
    component: ()=> import('./secure/Dashboard.vue')
},
{
    path: '/oath/panel',
    name: 'panel',
    meta: {layout:'SidebarNoOath', title: 'Base'},
    component: ()=> import('./secure/Dashboard.vue')
},

{
    path: '/oath/report',
    name: 'report',
    meta: {layout:'BackendHeader', title: 'Report'},
    component: ()=> import('./secure/Report.vue')
},

{
    path: '/oath/function_one',
    name: 'function_one',
    meta: {layout:'SidebarNoOath', title: 'function_one'},
    component: ()=> import('./secure/Function_one.vue')
},
{
    path: '/oath/template',
    name: 'template',
    meta: {layout:'SidebarNoOath', title: 'Template'},
    component: ()=> import('./views/template.vue')
},

]


})
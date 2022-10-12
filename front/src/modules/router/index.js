import Vue from "vue";
import Router from "vue-router";

const Login = () => import("../../pages/auth/Login");
const ForgotPassword = () => import("../../pages/auth/ForgotPassword");
const ResetPassword = () => import("../../pages/auth/ResetPassword");
const Main = () => import("../../pages/Home");
const About = () => import("../../pages/About");
const Account = () => import("../../pages/Account");
const Members = () => import("../../pages/Members");
const CreateMembers = () => import("../../pages/CreateMembers");

Vue.use(Router);

export default new Router({
  routes: [

    {
      path: '*',
      redirect: '/login'
    },
    {
      path: "/login",
      name: "login",
      meta: {
        hideHeader: true,
        transparentFooter: true
      },
      component: Login
    },
    {
      path: "/auth/email/forgot-password",
      name: "forgot-password",
      meta: {
        hideHeader: true,
        transparentFooter: true
      },
      component: ForgotPassword
    },
    {
      path: "/auth/email/reset-password/:token",
      name: "reset-password",
      meta: {
        hideHeader: true,
        transparentFooter: true
      },
      component: ResetPassword
    },
    {
      path: "/login/:token",
      name: "activate-account",
      meta: {
        hideHeader: true,
        transparentFooter: true
      },
      component: Login
    },
    {
      path: "/home",
      name: "home",
      meta: {},
      component: Main
    },
    {
      path: "/about",
      name: "about",
      meta: {},
      component: About
    },
    {
      path: "/accounts/:id",
      name: "account",
      meta: {
        transparentFooter: true
      },
      component: Account
    },
    {
      path: "/members",
      name: "members",
      meta: {
        transparentFooter: true
      },
      component: Members
    },
    {
      path: "/create-members",
      name: "create-members",
      meta: {
        transparentFooter: true
      },
      component: CreateMembers
    }
  ]
});
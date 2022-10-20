import {user, family, checkAuth, getUserInfo, getMemberInfo, logout} from './util'
import {loginWithEmail, signUpWithEmail, activateAccount} from './email'

export default {
  user,
  family,
  loginWithEmail,
  signUpWithEmail,
  activateAccount,
  checkAuth,
  logout,
  getUserInfo,
  getMemberInfo
}
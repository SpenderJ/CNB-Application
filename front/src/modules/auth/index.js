import {user, checkAuth, getUserInfo, logout} from './util'
import {loginWithEmail, signUpWithEmail, activateAccount} from './email'

export default {
  user,
  loginWithEmail,
  signUpWithEmail,
  activateAccount,
  checkAuth,
  logout,
  getUserInfo
}
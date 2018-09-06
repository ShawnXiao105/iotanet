import axios from 'axios'

export const list = (conditions = {}, pagination = { page: 1 }) => {
  return axios.get('/api/transaction', {
    params: { ...conditions, ...pagination }
  })
}
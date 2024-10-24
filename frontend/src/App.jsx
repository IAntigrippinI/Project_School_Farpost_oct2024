import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import AuthPage from './pages/mobile/auth/AuthPage'

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import MainPage from './pages/mobile/main/MainPage'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <div className='App'>


        <Routes>
          <Route path='/' element={<div className='container'><MainPage /></div>} />
          <Route path='/login' element={<div className='container'><AuthPage /></div>} />

        </Routes>
      </div>
      <div>
      </div>

    </Router>
  )


}

export default App

import './AuthPage.css'
import logo from './../../../images/logo.jpeg'
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

import Button from '../../../components/auth/Button/Button';
import ButtonLogin from '../../../components/auth/Button/ButtonLogin'
import InputFields from '../../../components/auth/InputFields/InputFields'

const AuthPage = () => {

    let api = 'http://127.0.0.1:8000/auth/login'
    let inactive_style = 'auth-btn-swch-inactive'
    let active_style = 'auth-btn-swch-active'
    const navigate = useNavigate()
    const [phone, setPhone] = useState('');
    const [password, setPassword] = useState('');
    const [isReg, setIsReg] = useState(0)



    function onChangePhone(e) {
        setPhone(e.target.value)
    }
    function onChangePassword(e) {
        setPassword(e.target.value)
    }

    function onClickLogin(e) {
        // const data = JSON.stringify({ phone: login, password: password });
        const data = {
            phone: phone,
            password: password,
        };
        axios.post(api, data, {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
        }).then((resp) => {
            // console.log(resp.data);

            document.cookie = 'access_token=' + resp.data.token
            navigate('/')
        }).catch((err) => {
            console.log(err)
        });
    }

    function onClickSwitchBtn(e) {
        console.log(e.target.innerText)
        if (e.target.innerText == 'Вход с паролем') {
            setIsReg(0)
        }
        else {
            setIsReg(1)
        }
    }

    return (
        <div className="auth">
            <div className="window-auth">
                <div className="auth-field">
                    <div className="logo">
                        <img className='logo-102' src={logo}></img>
                    </div>

                    <div className="auth-btns-switch">
                        <div className="auth-btn-block-1">
                            <Button onClick={onClickSwitchBtn} text={'Вход с паролем'} style={isReg ? inactive_style : active_style} />
                        </div>

                        <div className="auth-btn-block-2">
                            <Button onClick={onClickSwitchBtn} text={'Регистрация'} style={isReg ? active_style : inactive_style} />
                        </div>
                    </div>
                    {isReg ? <>
                        <div className="auth-inp-block">
                            <InputFields onChange={onChangePhone} description={'Телефон'} />
                        </div>
                        <div className="auth-btns-login-field">
                            <ButtonLogin onClick={onClickLogin} text={'Получить код'} style={'auth-btn-login-orange'} />
                            <ButtonLogin text={'Войти через телеграм'} style={'auth-btn-login-white'} />
                        </div>
                    </> : <> <div className="auth-inp-block">
                        <InputFields onChange={onChangePhone} description={'Телефон/Логин'} />
                        <InputFields onChange={onChangePassword} type={"password"} description={'Пароль'} />
                    </div>
                        <div className="auth-btns-login-field">
                            <ButtonLogin onClick={onClickLogin} text={'Войти'} style={'auth-btn-login-orange'} />
                            <ButtonLogin text={'Войти через телеграм'} style={'auth-btn-login-white'} />
                        </div></>}
                </div>
            </div>
        </div>

    );
}

export default AuthPage;
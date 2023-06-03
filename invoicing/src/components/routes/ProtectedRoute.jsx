import React,{useEffect} from "react";
import { useNavigate } from "react-router-dom";
const ProtectedRoute=(props)=>{
    const {Component}=props
    const navigat=useNavigate();
    useEffect(()=>{
        let token=localStorage.getItem('token')
        if(!token){
            navigat('/login')
        }
    },[]
    )
    return(
        <>
        <Component></Component>
        </>
    )
}
export default ProtectedRoute
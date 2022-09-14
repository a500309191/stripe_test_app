import { Routes, Route } from "react-router-dom";
import './App.scss';
import { ItemsList } from "./Components/ItemsList";
import { ItemDetails } from "./Components/ItemDetails";
import { PageNotFound } from "./Components/PageNotFound";;

export const App = () => {

    return (
        <div className="app">
            <Routes>
                <Route path='/' element={<ItemsList />}/>
                <Route path='/item/:item_id' element={<ItemDetails />}/>
                <Route path='*' element={<PageNotFound />}/>
            </Routes>
        </div>
    );
}

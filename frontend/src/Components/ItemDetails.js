import { useParams } from 'react-router-dom';
import { Link } from "react-router-dom";
import { Fetch } from "./Fetch";
import { ItemNotFound } from "./ItemNotFound";


export const ItemDetails = () => {
    const {item_id} = useParams();

    return (
        <Fetch
            uri = {`/api/items/${item_id}/`}
            renderSuccess = {ItemDetailsView}
        />
    )
}

const ItemDetailsView = ({data}) => {
    console.log(data)

    if (data.detail === "Not found.") {
        return (
            <ItemNotFound />
        )
    } else {
        return (
            <div className="item_details">
                <div className="item_details_name">
                    {data.name}
                </div>
                <div className="item_details_description">
                    <div>{data.description}</div>
                </div>
                <a href={`/buy/${data.id}`} className="buy_one_button">
                    BUY ONE  ({data.price/100}$)
                </a>
                <Link to={{pathname: `/`}} className="back_to">
                    BACK TO ITEMS LIST
                </Link>
            </div>
        )
    }
}
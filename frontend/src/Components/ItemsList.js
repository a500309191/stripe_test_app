import React, {useState } from "react";
import { Link } from "react-router-dom";
import { NoItems } from "./NoItems";
import { Fetch } from "./Fetch";


export const ItemsList = () => {
    return (
        <Fetch
            uri = '/api/items/'
            renderSuccess = {({ data }) => {
                if (data.length > 0) return <ItemsListView data={data}/>
                else return <NoItems />
            }}
        />
    )
}

export const ItemsListView = ({data}) => {

    const [bucketList, setBucketList] = useState([])
    const [itemsNumberDict, setItemsNumberDict] = useState({})

    const removeItemFromBucket = item => {
        setBucketList(bucketList.filter(i => i !== item))
    }
    const minus = (id) => {
        setItemsNumberDict(
            prev => {
                prev[id] === 1 ? removeItemFromBucket(id) : prev[id] -= 1
                return (
                    {...prev}
                )
            }
        )
    }
    const plus = (id) => {
        setItemsNumberDict(
            prev => {
                prev[id] += 1
                return (
                    {...prev}
                )
            }
        )
    }

    return (
        <div className="items_list_grid_window">
            <div class="items_titles">
                <div class="title_name">name:</div>
                <div class="title_price">price:</div>
                <div class="title_number">quantity:</div>
            </div>
            <div className="items_list">
                {data.map((item, index) => {
                    let id = item.id
                    return (
                        <div className="item_line" key={index}>
                            <Link className="item" to={{pathname: `/item/${item.id}`}}>   
                                <div className="item_name"><div>{item.name}</div></div>
                                <div className="item_price">{item.price / 100}${item.currency}</div>
                            </Link>
                            <div
                                className={`${bucketList.includes(id) ? "remove_button" : "add_button"}`}
                                onClick={() => {
                                    setItemsNumberDict(prev => {return { ...prev, [id]: 1 }})
                                    bucketList.includes(id)
                                        ? setBucketList(bucketList.filter(i => i !== id))
                                        : setBucketList([...bucketList, id])
                                    }
                                }
                            >
                                {`${bucketList.includes(id) ? "REMOVE" : "ADD"}`}
                            </div>
                            <div className={`${bucketList.includes(id) ? "item_counter" : "hide_item_counter"}`}>
                                <div className="minus_button" onClick={() => minus(id)}>-</div>
                                <div className="item_number">{itemsNumberDict[id]}</div>
                                <div className="plus_button" onClick={() => plus(id)}>+</div>
                            </div>
                        </div>
                    )
                })}
            </div>
            <div className="buy-all_block">
                <a
                    className="buy-all_button"
                    href={`buy_bunch/${bucketList.map((id, _) => `${id}n${itemsNumberDict[id]}`).join('+')}`}
                >
                    BUY ALL
                </a>
                <div className="item_total_cost">
                    {data.filter(item => bucketList.includes(item.id)).map((item, _) => item.price*itemsNumberDict[item.id]).reduce((a, b) => a + b, 0)/100}$
                </div>
                <div className="item_total_amount">
                    {bucketList.map((id, _) => itemsNumberDict[id]).reduce((a, b) => a + b, 0)}x
                </div>
            </div>
            <div className="bucket_list">
                {
                    data.filter(item => bucketList.includes(item["id"])).map(
                        (item, index) => {
                            let id = itemsNumberDict[item.id]
                            let name = item.name
                            return (
                                <div
                                    key={index}
                                    onClick={() => removeItemFromBucket(item.id)}
                                >
                                    <div className="bucket_list_item_name">
                                        {name}
                                    </div>
                                    <div
                                        className="bucket_list_item_number"
                                        className={`${id > 1 ? "bucket_list_item_number" : "hide_bucket_list_item_number"}`}
                                    >
                                        {id}
                                    </div>
                                </div>
                            )
                        }
                    )
                }
            </div>
        </div>
    )
}


import httpx
from typing import Any, Dict, Optional, Set
from ..settings import BASE_URL_API


class APIClient:
    def __init__(self, base_url: str = BASE_URL_API):
        self.base_url = base_url

    async def _request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None,
                       params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        if params is not None:
            url += "?" + "&".join(list(map(lambda x: f"{x[0]}={x[1]}", params.items())))
        async with httpx.AsyncClient() as client:
            response = await client.request(method, url, json=data)
            response.raise_for_status()
            return response.json()

    async def create_feedback(self, user_id: int, text: str) -> Dict[str, Any]:
        data = {
            "user_id": user_id,
            "text": text
        }
        return await self._request("POST", "/feedback/", data)

    async def get_feedback(self, feedback_id: int) -> Dict[str, Any]:
        return await self._request("POST", f"/feedback/{feedback_id}")

    async def update_feedback(self, feedback_id: int, answer: Optional[str] = None) -> Dict[str, Any]:
        data = {}
        if answer is not None:
            data["answer"] = answer
        return await self._request("PUT", f"/feedback/{feedback_id}", data)

    async def create_user(self, full_name: str, address: str, tg_id: int, username: str) -> Dict[str, Any]:
        data = {
            "full_name": full_name,
            "address": address,
            "tg_id": tg_id,
            "username": username
        }
        return await self._request("POST", "/user/", data)

    async def get_user(self, user_id: int) -> Dict[str, Any]:
        return await self._request("GET", f"/user/{user_id}")

    async def update_user(self, user_id: int, full_name: Optional[str] = None, address: Optional[str] = None,
                          tg_id: Optional[int] = None, username: Optional[str] = None) -> Dict[str, Any]:
        data = {}
        if full_name is not None:
            data["full_name"] = full_name
        if address is not None:
            data["address"] = address
        if tg_id is not None:
            data["tg_id"] = tg_id
        if username is not None:
            data["username"] = username
        return await self._request("PUT", f"/user/{user_id}", data)

    async def delete_user(self, user_id: int) -> Dict[str, Any]:
        return await self._request("DELETE", f"/user/{user_id}")

    async def get_filter_users(self, full_name: Optional[str] = None, address: Optional[str] = None,
                               tg_id: Optional[int] = None) -> Dict[str, Any]:
        params = {}
        if full_name is not None:
            params["full_name"] = full_name
        if address is not None:
            params["address"] = address
        if tg_id is not None:
            params["tg_id"] = tg_id
        return await self._request("GET", "/user/", params=params)

    async def create_order(self, user_id: int, product_url: str, order_status: str = 0) -> Dict[str, Any]:
        data = {
            "user_id": user_id,
            "product_url": product_url,
            "order_status": order_status
        }
        return await self._request("POST", "/order/", data)

    async def get_order(self, order_id: int) -> Dict[str, Any]:
        return await self._request(" GET", f"/order/{order_id}")

    async def update_order(self, order_id: int, user_id: Optional[int] = None, product_url: Optional[str] = None,
                           order_status: Optional[int] = None) -> Dict[str, Any]:
        data = {}
        if user_id is not None:
            data["user_id"] = user_id
        if product_url is not None:
            data["product_url"] = product_url
        if order_status is not None:
            data["order_status"] = order_status
        return await self._request("PUT", f"/order/{order_id}", data)

    async def delete_order(self, order_id: int) -> Dict[str, Any]:
        return await self._request("DELETE", f"/order/{order_id}")

    async def get_filter_orders(self, user_id: Optional[int] = None, product_url: Optional[str] = None,
                                order_status: Optional[str] = None, today: bool = False) -> Dict[str, Any]:
        params = {}
        if user_id is not None:
            params["user_id"] = user_id
        if product_url is not None:
            params["product_url"] = product_url
        if order_status is not None:
            params["order_status"] = order_status
        if today:
            params["today"] = today
        return await self._request("GET", "/order/", params=params)

    async def create_role(self, role_name: str) -> Dict[str, Any]:
        data = {
            "role_name": role_name
        }
        return await self._request("POST", "/role/", data)

    async def get_role(self, role_id: int) -> Dict[str, Any]:
        return await self._request("GET", f"/role/{role_id}")

    async def update_role(self, role_id: int, role_name: Optional[str] = None) -> Dict[str, Any]:
        data = {}
        if role_name is not None:
            data["role_name"] = role_name
        return await self._request("PUT", f"/role/{role_id}", data)

    async def delete_role(self, role_id: int) -> Dict[str, Any]:
        return await self._request("DELETE", f"/role/{role_id}")

    async def get_filter_roles(self, role_name: Optional[str] = None) -> Dict[str, Any]:
        params = {}
        if role_name is not None:
            params["role_name"] = role_name
        return await self._request("GET", "/role/", params=params)

    async def assign_role_to_user(self, user_id: int, role_id: int) -> Dict[str, Any]:
        data = {
            "user_id": user_id,
            "role_id": role_id
        }
        return await self._request("POST", "/user_role/", data)

    async def get_user_roles(self, user_id: int) -> Dict[str, Any]:
        return await self._request("GET", f"/user_role/{user_id}")

    async def get_filter_user_roles(self, user_id: Optional[int] = None, role_id: Optional[int] = None) -> Dict[
        str, Any]:
        params = {}
        if user_id is not None:
            params["user_id"] = user_id
        if role_id is not None:
            params["role_id"] = role_id
        return await self._request("GET", "/user_role/", params=params)

    async def remove_role_from_user(self, user_id: int, role_id: int) -> Dict[str, Any]:
        return await self._request("DELETE", f"/user_role/{user_id}/{role_id}")

    async def create_item(self, name: str, address: Optional[str] = None, price: Optional[float] = None,
                          tags: Optional[Set[str]] = None, start_datetime: Optional[str] = None) -> Dict[str, Any]:
        data = {
            "name": name,
            "address": address,
            "price": price,
            "tags": list(tags) if tags else [],
            "start_datetime": start_datetime
        }
        return await self._request("POST", "/items/", data)

    async def get_item(self, item_id: int) -> Dict[str, Any]:
        return await self._request("GET", f"/items/{item_id}")

    async def update_item(self, item_id: int, name: Optional[str] = None, address: Optional[str] = None,
                          price: Optional[float] = None, tags: Optional[Set[str]] = None,
                          start_datetime: Optional[str] = None) -> Dict[str, Any]:
        data = {}
        if name is not None:
            data["name"] = name
        if address is not None:
            data["address"] = address
        if price is not None:
            data["price"] = price
        if tags is not None:
            data["tags"] = list(tags)
        if start_datetime is not None:
            data["start_datetime"] = start_datetime
        return await self._request("PUT", f"/items/{item_id}", data)

    async def delete_item(self, item_id: int) -> Dict[str, Any]:
        return await self._request("DELETE", f"/items/{item_id}")

    async def get_filter_items(self, address: Optional[str] = None, tags: Optional[Set[str]] = None,
                               price: Optional[float] = None, today: bool = False) -> Dict[str, Any]:
        params = {}
        if address is not None:
            params["address"] = address
        if tags is not None:
            params["tags"] = list(tags)
        if price is not None:
            params["price"] = price
        if today:
            params["today"] = today
        return await self._request("GET", "/items/", params=params)

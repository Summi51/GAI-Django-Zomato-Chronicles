from django.shortcuts import render, redirect
from django.http import HttpResponse

DATA_BASE = {
  "menu": [
    {
      "id": 1,
      "name": "Pastaa",
      "price": 99,
      "available": true,
      "description": "Authentic Italian pasta."
    },
    {
      "id": 2,
      "name": "Pizza",
      "price": 245,
      "available": false,
      "description": "Delicious pizza with a variety."
    },
    {
      "id": 3,
      "name": "Burger",
      "price": 90,
      "available": true,
      "description": "Classic burger with a variety."
    },
    {
      "id": 4,
      "name": "Dosa",
      "price": 129,
      "available": true,
      "description": "simple dosa with a variety."
    },
    {
      "id": 5,
      "name": "Maggi",
      "price": 40,
      "available": true,
      "description": "Maggi with cheese."
    },
    {
      "id": 6,
      "name": "Manchurian",
      "price": 234,
      "available": true,
      "description": "Manchurian with a variety."
    },
    {
      "id": 7,
      "name": "Sandwich",
      "price": 150,
      "available": true,
      "description": "Classic sandwich with a variety."
    },
    {
      "id": 8,
      "name": "White Sos Pasta",
      "price": 149,
      "available": true,
      "description": "White Sos pasta very tasty with a variety of sauce."
    },
    {
      "id": 9,
      "name": "Paneer Tikka",
      "price": 255,
      "available": true,
      "description": "Paneer Tikka with a variety of sauce."
    },
    {
      "id": 10,
      "name": "Soda",
      "price": 20,
      "available": true,
      "description": "Refreshing drinks including juices, sodas"
    },
    {
      "id": 11,
      "name": "French Fries",
      "price": 100,
      "available": true,
      "description": "French Fries with cheese."
    },
    {
      "id": 12,
      "name": "Sweet Corn",
      "price": 146,
      "available": true,
      "description": "Sweet Corn with cheese."
    },
    {
      "id": 13,
      "name": "Cake",
      "price": 500,
      "available": true,
      "description": "Chocklate Cake."
    },
    {
      "id": 14,
      "name": "Icecream",
      "price": 157,
      "available": true,
      "description": "Icecream with a variety."
    },
    {
      "id": 15,
      "name": "Shake",
      "price": 250,
      "available": true,
      "description": "Shake with a variety."
    }
  ],
  "orders": [
    {
      "id": 1,
      "customer_name": "Doein Smith",
      "dishes": [
        {
          "id": 2,
          "name": "Pizza",
          "price": 245
        },
        {
          "id": 3,
          "name": "Burger",
          "price": 90
        }
      ],
      "status": "delivered",
      "total_price": 335
    },
    {
      "id": 2,
      "customer_name": "John Doe",
      "dishes": [
        {
          "id": 5,
          "name": "Maggi",
          "price": 40
        },
        {
          "id": 6,
          "name": "Manchurian",
          "price": 234
        },
        {
          "id": 14,
          "name": "Icecream",
          "price": 157
        }
      ],
      "status": "preparing",
      "total_price": 431
    },
    {
      "id": 3,
      "customer_name": "Stefan Kowalski",
      "dishes": [
        {
          "id": 7,
          "name": "Sandwich",
          "price": 150
        }
      ],
      "status": "preparing",
      "total_price": 150
    },
    {
      "id": 4,
      "customer_name": "Samreen Inayat",
      "dishes": [
        {
          "id": 2,
          "name": "Pizza",
          "price": 245
        },
        {
          "id": 4,
          "name": "Dosa",
          "price": 129
        },
        {
          "id": 7,
          "name": "Sandwich",
          "price": 150
        }
      ],
      "status": "delivered",
      "total_price": 524
    },
    {
      "id": 5,
      "customer_name": "Demon King",
      "dishes": [
        {
          "id": 15,
          "name": "Shake",
          "price": 250
        },
        {
          "id": 12,
          "name": "Sweet Corn",
          "price": 146
        },
        {
          "id": 13,
          "name": "Cake",
          "price": 500
        },
        {
          "id": 8,
          "name": "White Sos Pasta",
          "price": 149
        }
      ],
      "status": "delivered",
      "total_price": 1045
    },
    {
      "id": 6,
      "customer_name": "Elena Petrova",
      "dishes": [
        {
          "id": 10,
          "name": "Soda",
          "price": 20
        }
      ],
      "status": "delivered",
      "total_price": 20
    },
    {
      "id": 7,
      "customer_name": "Nina Doe",
      "dishes": [
        {
          "id": 9,
          "name": "Paneer Tikka",
          "price": 255
        },
        {
          "id": 11,
          "name": "French Fries",
          "price": 100
        }
      ],
      "status": "preparing",
      "total_price": 355
    }
  ]
}

def dish_read(request):
   menu = DATA_BASE["menu"]
   return render(request, "zomatoapp.html", {"menu": menu})


def dish_edit(request, dish_id):
   if request.method == "POST":
    menu = DATA_BASE["menu"]
    orders = DATA_BASE["orders"]
    dish = menu[int(dish_id) - 1]
    dish["name"] = request.POST.get("name")
    dish["price"] = request.POST.get("price")
    dish['available'] = [True if request.POST.get("available") == "on" else False][
        0
    ]
    dish["description"] = request.POST.get("description")
    DATA_BASE["menu"] = menu
    DATA_BASE["orders"] = orders
    return redirect("zomatoapp")
   else:
    menu = DATA_BASE["menu"]
    dish = menu[dish_id-1] 
    return render(request, "update.html", {"dish": dish})

def dish_add(request):
   if request.method == "POST":
    menu = DATA_BASE["menu"]
    orders = DATA_BASE["orders"]
    new_dish = {
      "id": len(menu) + 1,
      "name": request.POST.get("name"),
      "price": float(request.POST.get("price")),
      "available": False,
      "description": request.POST.get("description")
    }
    
    if new_dish["name"] == "":
        return HttpResponse("Name can't be empty")
    if new_dish["price"] == "":
        return HttpResponse("Price can't be empty")
    if new_dish["description"] == "":
        return HttpResponse("Description can't be empty")
 
   menu.append(new_dish)
   DATA_BASE["menu"] = menu
   DATA_BASE["orders"] = orders
   return redirect("zomatoapp")

return render(request, "dish_add.html")


def orders(request):
    orders = DATA_BASE["orders"]
    return render(
        request,
        "orders.html",
        {"orders": orders},
    )

def update_order_status(request, order_id):
    if request.method == "POST":
        menu = DATA_BASE["menu"]
        orders = DATA_BASE["orders"]
        order = orders[order_id - 1]
        order["status"] = request.POST.get("status")
        DATA_BASE["menu"] = menu
        DATA_BASE["orders"] = orders
        return redirect("orders")
    else:
        orders = DATA_BASE["orders"]
        order = orders[order_id - 1]
        return render(
            request,
            "update_order_status.html",
            {"order": order},
        )


def place_order(request, dish_id):
    menu = DATA_BASE["menu"]
    orders = DATA_BASE["orders"]
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        selected_dishes = request.POST.getlist("selected_dishes[]")

      
        selected_dishes = [int(dish_id) for dish_id in selected_dishes]

        new_order = {
            "id": len(orders) + 1,
            "customer_name": customer_name,
            "dishes": [menu[dish_id - 1] for dish_id in selected_dishes],
            "status": "received",
            "total_price": sum(
                menu[dish_id - 1]["price"] for dish_id in selected_dishes
            ),
        }

        print(new_order)
        DATA_BASE["orders"].append(new_order)
        DATA_BASE["menu"] = menu

        return redirect("orders")

    return render(request, "place_order.html", {"current_id": dish_id, "menu": menu})


def dish_search(request):
    query = request.GET.get("search")
    menu = DATA_BASE["menu"]

    if query:
        search_results = [
            dish for dish in menu if query.lower() in dish["name"].lower()
        ]
    else:
        search_results = menu

    return render(request, "zomatoapp.html", {"menu": search_results, "query": query})


def dish_delete(request, dish_id):
    menu = DATA_BASE["menu"]
    menu.pop(dish_id - 1)
    DATA_BASE["menu"] = menu
    return redirect("zomatoapp")
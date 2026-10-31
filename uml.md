# UML class diagram (Mermaid)

Render at https://mermaid.live, then redraw in your lecture's notation
(<<abstract>> label, italics for abstract methods).

```mermaid
classDiagram
    class Product {
        <<abstract>>
        -product_id
        -name
        -price
        -stock
        +update_stock(new_quantity)
        +display_information()
        +to_dict() dict
        +get_fulfilment_info()* str
    }
    class CanBeShipped {
        <<interface>>
        +calculate_shipping_cost()* float
    }
    class PhysicalProduct {
        -weight
        +display_information()
        +get_fulfilment_info() str
        +calculate_shipping_cost() float
        +to_dict() dict
        +from_dict(data)$ PhysicalProduct
    }
    class DigitalProduct {
        -download_size
        +display_information()
        +get_fulfilment_info() str
        +to_dict() dict
        +from_dict(data)$ DigitalProduct
    }
    class Inventory {
        -products
        +add_product(product)
        +get_product(product_id)
        +update_stock(product_id, new_quantity)
        +display_all()
        +load(filename)
        +save(filename)
    }
    Product <|-- PhysicalProduct : inheritance
    Product <|-- DigitalProduct : inheritance
    CanBeShipped <|.. PhysicalProduct : realisation
    Inventory o-- "0..*" Product : manages
```

Notation reminders:
- Inheritance: SOLID line, hollow triangle at Product.
- Interface realisation: DASHED line, hollow triangle at CanBeShipped (PhysicalProduct only).
- Inventory to Product: association/aggregation with 0..* at the Product end.

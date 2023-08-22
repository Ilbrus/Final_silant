# Дипломная работа SkillFactory

### Пользователи
- **Клиент** - имеет доступ к данным определённых машин. У каждой машины есть только один клиент
- **Сервисная организация** - имеет доступ к данным определённых машин. У каждой машины только одна сервисная организация
- **Менеджер** - имеет доступ к данным по всем машинам, а также имеет возможность редактировать справочники
- **Администратор** - имеет доступ ко всем данным

### API
В данной системе предусмотрено использование API запросы. Полученные данные возвращаются в формате json.
#### Машины
```
api/cars/ - Получение всех машин
```
api/car/{id}/ - Получение машины по индентификатору
```
api/{user}/cars/ - Получение машин конкретного пользователя
```
| Параметр | Тип | Описание |
|:-|:-:|:-|
| id | integer | Индентификатор |
| car_number | string | Зав. № машины |
| technic | list | Модель техники |
| engine | list | Модель двигателя |
| engine_number | string | Зав. № двигателя |
| transmission | list | Модель трансмиссии |
| transmission_number | string | Зав. № трансмиссии |
| driving_bridge | list | Модель ведущего моста |
| driving_bridge_number | string | Зав. № ведущего моста |
| controlled_bridge | list | Модель управляемого моста |
| controlled_bridge_number | string | Зав. № управляемого моста |
| delivery_contract | string | Договор поставки №, дата |
| date_shipment | date | Дата отгрузки с завода |
| consignee | string | Грузополучатель (конечный потребитель) |
| delivery_address | string | Адрес поставки (эксплуатации) |
| equipment | string | Комплектация (доп. опции) |
| client | list | Клиент |
| service_company | list | Сервисная компания |
#### Техническое обслуживание
```
api/maintenances/ - Получение всей истории технического обслуживания
```
api/maintenance/{id}/ - Получение конкретного технического обслуживания по индентификатору
```
api/{user}/maintenances/ - Получение истории технического обслуживания для пользователя
```
| Параметр | Тип | Описание |
|:-|:-:|:-|
| id | integer | Индентификатор |
| type | list | Вид ТО |
| date | date | Дата проведения ТО |
| operating_time | integer | Наработка, м/час |
| order_number | string | № заказ-наряда |
| order_date | date | Дата заказ-наряда |
| service_company | list | Организация, проводившая ТО |
| car | list | Сервисная компания |
#### Рекламации
```
api/complaints/ - Получение всех рекламаций
```
api/complaint/{id}/ - Получение конкретной рекламации по индентификатору
```
api/{user}/complaints/ - Получение всех рекламаций для пользователя
```
| Параметр | Тип | Описание |
|:-|:-:|:-|
| id | integer | Индентификатор |
| date_failure | date | Дата отказа |
| operating_time | integer | Наработка, м/час |
| node_failure | list | Узел отказа |
| description_failure | string | Описание отказа |
| method_recovery | list | Способ восстановления |
| repair_parts | string | Используемые запасные части |
| date_recovery | date | Дата восстановления |
| car | list | Машина |
| service_company | list | Сервисная компания |
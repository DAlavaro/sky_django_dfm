## Задание 1
Подключите СУБД PostgreSQL для работы в проекте. Для этого:
- [x] Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром. На странице с товаром необходимо вывести всю информацию о товаре.
	*Для создания шаблонов используйте UI kit Bootstrap. При возникновении проблем возьмите за основу [данный шаблон](https://github.com/oscarbotru/skystore-templates).*
## Задание 2
- [x] В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание обрежьте после первых выведенных 100 символов.
## Задание 3
- [x] Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон и также подшаблон с главным меню.
	*При необходимости можно выделить больше общих шаблонов.*
## Задание 4
Для выводимого изображения на странице реализуйте шаблонный фильтр, который преобразует переданный путь в полный путь для доступа к медиафайлу:
```html
<!-- Исходный вариант -->
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{{ object.image|mediapath }}" />
```
Реализуйте описанный функционал с помощью шаблонного тега:
```html
<!-- Исходный вариант -->
<img src="/media/{{ object.image }}" /> 
<!-- Итоговый вариант -->
<img src="{% mediapath object.image %}" />
```
## *Дополнительное задание*
- Добавьте функционал создания продукта через внешний интерфейс, не используя стандартную админку.
- Реализуйте постраничный вывод списка продуктов.<br>
Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.
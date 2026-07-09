INSERT INTO users (username) VALUES ('Артём');
INSERT INTO users (username) VALUES ('Мария');
INSERT INTO users (username) VALUES ('Иван');

INSERT INTO categories (name) VALUES ('Еда');
INSERT INTO categories (name) VALUES ('Транспорт');
INSERT INTO categories (name) VALUES ('Развлечения');
INSERT INTO categories (name) VALUES ('Здоровье');

INSERT INTO transactions (user_id, category_id, amount, type) VALUES (1, 1, 1000.0, 'expense');
INSERT INTO transactions (user_id, category_id, amount, type) VALUES (2, 2, 1000.0, 'expense');
INSERT INTO transactions (user_id, category_id, amount, type) VALUES (2, 4, 1000.0, 'income');
INSERT INTO transactions (user_id, category_id, amount, type) VALUES (3, 1, 1000.0, 'expense');
INSERT INTO transactions (user_id, category_id, amount, type) VALUES (3, 4, 1000.0, 'income');
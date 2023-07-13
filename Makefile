# タスクを指定しないmakeの実行を禁止する.
all:
	echo "make単体での実行は禁止されています.タスクを指定して実行して下さい."
	exit 1

# サーバーを起動する.
run_server:
	cd src && python manage.py runserver

run_with_docker:
	docker-compose up

build_and_run_with_docker:
	docker-compose build --no-cache && docker-compose up

# フロントエンドの環境構築.
setup_frontend:
	cd src/frontend && npm i

# JSをビルドする.
build_js:
	rm -f src/static_files/static/bundles/*js
	cd src/frontend && npm run build

collect_static:
	docker exec -it canal_server bash -c "cd /suez/src && python manage.py collectstatic --noinput"

compile_scss:
	docker exec -it canal_server bash -c "cd /suez/src && python manage.py compilescss"

# Dockerコンテナ内のDBを更新する
SQL?=testdata.sql
docker_db_update:
	docker exec -it canal_db bash -c "mysql -u canallocal --password=hogehoge canal < /suez/fixtures/${SQL}"

# JSをwatchする.
watch_js:
	rm -f src/static_files/static/bundles/*js
	cd src/frontend && npm run watch

# DBのマイグレーションを実行する.
migrate:
	docker exec -it canal_server bash -c "cd /suez/src && python manage.py migrate"

# 商品情報(extra_info)をjson化 + DBに入れる
update_product_info:
	cd product_data && ./create_data.sh && cd ..

# 商品のextra_infoデータをDBに取り込む
import_product_info:
	cd src && python manage.py import_extra_data

# super userを生成する.
create_superuser:
	cd src && python manage.py createsuperuser

# svgセットアップ.
setup_svg:
	cd svg && bundle i

# svg生成.
gen_svg_sprites:
	cd svg && bundle exec svgeez build --source sprites --destination icons.svg
	mv -f svg/icons.svg src/templates/svg.html
	rm -f svg/icons.svg

import_product_fixtures:
	docker exec -it canal_db bash -c "/suez/commands/import_products.sh"

# mysqlにログイン.
login_mysql:
	docker exec -it canal_db bash -c "mysql -u canallocal --password=hogehoge"

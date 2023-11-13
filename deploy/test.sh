echo "Setting up initial data..."
echo "Creating initial user..."
password=`9cqvywxoqo`
echo '' | docker compose exec --no-TTY -e DJANGO_SUPERUSER_USERNAME="root" -e DJANGO_SUPERUSER_PASSWORD="$password" app python3 manage.py createsuperuser --noinput
echo ""
echo "Very nice."
echo "You can now login at http://127.0.0.1:8000"
echo "Username: reptor"
echo "Password: $password"

echo "Importing demo projects..."
url="https://docs.sysreptor.com/assets/demo-projects.tar.gz"
curl -s "$url" | docker compose exec --no-TTY app python3 manage.py importdemodata --type=project --add-member=reptor
echo "Importing demo designs..."
url="https://docs.sysreptor.com/assets/demo-designs.tar.gz"
curl -s "$url" | docker compose exec --no-TTY app python3 manage.py importdemodata --type=design
echo "Importing finding templates..."
url="https://docs.sysreptor.com/assets/demo-templates.tar.gz"
curl -s "$url" | docker compose exec --no-TTY app python3 manage.py importdemodata --type=template
echo "All imported."

echo ""
echo "Very nice."
echo "You can now login at http://127.0.0.1:8000"
echo "Username: reptor"
echo "Password: $password"

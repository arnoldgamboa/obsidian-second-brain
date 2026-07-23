> # Create the mu-plugins directory if it doesn't exist
> mkdir -p /var/www/html/wp-content/mu-plugins

> # Create the plugin file
> cat > /var/www/html/wp-content/mu-plugins/force-ssl.php <<'EOF'
> <?php
> /**
 > * Plugin Name: Force SSL Detection
 > * Description: Forces SSL detection behind reverse proxy
 > */

> // Set before WordPress loads
> $_SERVER\['HTTPS'\] = 'on';
> $_SERVER\['SERVER_PORT'\] = 443;

> if (isset($_SERVER\['HTTP_X_FORWARDED_PROTO'\]) && $_SERVER\['HTTP_X_FORWARDED_PROTO'\] === 'https') {
    > $_SERVER\['HTTPS'\] = 'on';
> }

> if (isset($_SERVER\['HTTP_X_FORWARDED_HOST'\])) {
    > $_SERVER\['HTTP_HOST'\] = $_SERVER\['HTTP_X_FORWARDED_HOST'\];
> }
> EOF
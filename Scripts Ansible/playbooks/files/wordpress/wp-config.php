<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpressdb' );

/** MySQL database username */
define( 'DB_USER', 'wordpressuser' );

/** MySQL database password */
define( 'DB_PASSWORD', 'wordpress' );

/** MySQL hostname */
define( 'DB_HOST', '127.0.0.1' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '7a+/EU59nhE>p,-Q^@=^VH`0NeC~GnZJ]LF:gm,5262BiZTb,I!i7Ebi2Y]&pCm#' );
define( 'SECURE_AUTH_KEY',  ':,)W DYBP?8}zyeQdc<{)9l  (/5ypory[|qNTcA=:JQpi_Wx?=P)tK>/>,mhP]E' );
define( 'LOGGED_IN_KEY',    'T`kWTBPOXZ6Zp Zk^@A9lU<ROxcX^HOOMFFl0Qn,?4IZq~k(#g{/jx48X}-j8Jjv' );
define( 'NONCE_KEY',        'a/#*wsAZA.T32_J0w6g*G_GIE~Vu`NNI)dmsZz *1H?]%1%0b%A,?wL8]!6~$Ot[' );
define( 'AUTH_SALT',        'UK6hG6v- yMk8>TcycFlN?Ts_-8bz:gY:or Wh]]#ZxN$Ou]]x6mZ+a}5Rj&MLXO' );
define( 'SECURE_AUTH_SALT', 'ZF<HIC8-v1{0K4M`K%;UX0qNMg{83L7;GS$s(%M#=s+bzrK3uxJYXZ*L_s2m{)~j' );
define( 'LOGGED_IN_SALT',   '3v}HE-k5SDakPx/)nOhp%;nm@OzAY%f35[Wd]9~EF=]&P&sbOFG#LgH8xM,_b_W(' );
define( 'NONCE_SALT',       'X8WxXz33H|lzTm<`yK&;*0ZvLv%dp-ej?WZrtWKysu#J6Oamf*IMHzv%Q/`gs[-m' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once( ABSPATH . 'wp-settings.php' );


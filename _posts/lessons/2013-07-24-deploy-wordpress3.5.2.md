---
layout: post
category: lessons
tagline: on SAE(sina app engine)
tags: [wordpress,tutorial]
---

#### wp-config.php
```php
<?php
define('DB_NAME', SAE_MYSQL_DB);
define('DB_USER', SAE_MYSQL_USER);
define('DB_PASSWORD', SAE_MYSQL_PASS);
define('DB_HOST', SAE_MYSQL_HOST_M.':'.SAE_MYSQL_PORT);

//--- the following constant would be referenced later in wp-include/functions.php ---
define('SAE',true);
/** SAE Storage Domain */
define('SAE_STORAGE', wordpress);
/** File Upload Dir */
define('SAE_DIR','saestor://'.SAE_STORAGE.'/uploads');
/** File URL PATH */
define('SAE_URL', 'http://' . $_SERVER['HTTP_APPNAME'] . '-'.SAE_STORAGE.'.stor.sinaapp.com/uploads');
```

<!--excerpt:end-->
#### disable chmod file
wp-admin/includes/file.php(2)、wp-include/class-wp-image-editor-gd.php(1)

```php
<?php
if(!defined('SAE')){
    $stat = stat( dirname( $new_file ));
    $perms = $stat['mode'] & 0000666;
    @chmod( $new_file, $perms );
}
```

#### change the default upload directory and attachment download url
wp-includes/functions.php 

```php
<?php
function wp_upload_dir( $time = null ) {
    //codes ...
   if(defined('SAE')){
       $dir = SAE_DIR;
       $url = SAE_URL;
    }
	$basedir = $dir;
	$baseurl = $url;
}
function wp_mkdir_p( $target ) {
   if(defined('SAE')){
         return substr($target, 0, 10) == 'saestor://';
   }
    //more codes here ...
}
```

#### [optional]disable auto update
wp-include/update.php, move to the bottom of file,  comment out all of `add_action`, except the line:
`add_action( 'load-update-core.php', 'wp_update_plugins' );`

#### [optional][fix thumbnail](http://www.xiumu.org/diary/wordpress-for-sae.shtml), reimplement cache with KVDB(KVDB is much cheaper than memcache)

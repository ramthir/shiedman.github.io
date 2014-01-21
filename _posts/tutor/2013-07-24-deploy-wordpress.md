---
layout: post
category: tutor
title: Deploy wordpress on SAE 
#tagline: on SAE(sina app engine)
tags: [wordpress,tutorial]
---

**NOTE**: This tutor work on wordpress 3.5.x to 3.8.x

#### wp-config.php

{% highlight php startinline %}
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
{% endhighlight %}

<!--more-->

#### disable chmod file

wp-admin/includes/file.php(2)、wp-include/class-wp-image-editor-gd.php(1)

{% highlight php startinline %}
if(!defined('SAE')){
    $stat = stat( dirname( $new_file ));
    $perms = $stat['mode'] & 0000666;
    @chmod( $new_file, $perms );
}
{% endhighlight %}

#### change the default upload directory and attachment download url
wp-includes/functions.php

{% highlight php startinline %}
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
{% endhighlight %}

#### [optional]add memcache support
download [Memcached Object Cache](http://wordpress.org/plugins/memcached/), change source as the following, put `object-cache.php` to dir `wp-content` 

{% highlight php startinline %}
function WP_Object_Cache() {
    //codes here ...
    foreach ( $buckets as $bucket => $servers) {
        $this->mc[$bucket] = memcache_init();//SAE memcache
        /*
        $this->mc[$bucket] = new Memcache();
        foreach ( $servers as $server  ) {
            list ( $node, $port ) = explode(':', $server);
            if ( !$port )
                $port = ini_get('memcache.default_port');
            $port = intval($port);
            if ( !$port )
                $port = 11211;
            $this->mc[$bucket]->addServer($node, $port, true, 1, 1, 15, true, array($this, 'failure_callback'));
            $this->mc[$bucket]->setCompressThreshold(20000, 0.2);
        }
        */
    }

{% endhighlight %}

#### [optional]disable auto update
wp-include/update.php, move to the bottom of file,  comment out all of `add_action`, except the line:
{% highlight php startinline %}
add_action( 'load-update-core.php', 'wp_update_plugins' );
{% endhighlight %}


#### [optional][fix thumbnail](http://www.xiumu.org/diary/wordpress-for-sae.shtml), reimplement cache with KVDB(KVDB is much cheaper than memcache)

## Tools

Get upgrade path

https://gitlab-com.gitlab.io/support/toolbox/upgrade-path/


## Filesystem

sudo mkfs.xfs /dev/sdb

sudo mkdir -p /mnt/gitlab

sudo mount /dev/sdb /mnt/gitlab

sudo chown -R YOURUSER:YOURUSER /mnt/gitlab

sudo chmod 700 /mnt/gitlab

sudo blkid (find disk id)	

sudo nano /etc/fstab

UUID=4ae284f2-898f-46ff-98c4-98c5381668f2    /mnt/gitlab   xfs    rw,relatime,discard   0    2


## S3 Registry:

registry['storage'] = {

 's3_v2' => {
 
   'accesskey' => '<s3-access-key>',
   
   'secretkey' => '<s3-secret-key-for-access-key>',
   
   'bucket' => '<your-s3-bucket>',
   
   'region' => '<your-s3-region>',
   
   'regionendpoint' => '<your-s3-regionendpoint>',
   
   'checksum_disabled' => true
   
   'maxrequestspersecond' => 100
   
 }
 
}

https://docs.gitlab.com/administration/packages/container_registry/#use-object-storage



## For non traefik instance add:

    ports:
      - '443:443'
      - '5005:5005'

And remove labels and proxy network



## Migration/Restore/backup: (copy files over with right file permsisions and user permissions)

Run: 

gitlab-backup create

/var/opt/gitlab/backup

Copy .tar file


Copy theese form config:

/srv/gitlab/config/

gitlab-secrets.json  gitlab.rb


Registry:

/var/opt/gitlab/gitlab-rails/shared/registry (copy over the registry your want)

On new host run: gitlab-backup create restore
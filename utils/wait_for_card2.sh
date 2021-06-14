while true
do
  num=$(ps "$1" | wc -l)
  if [ $num -lt 2 ];
  then
    break
  else
    echo "sleep 5 seconds"
    sleep 5
  fi
done

cd ..

python3 train.py --config-file=configs/abbd_iter_7.yaml --log_step=50 --save_step=20000 --eval_step=-1


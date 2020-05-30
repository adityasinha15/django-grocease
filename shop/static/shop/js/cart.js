<script>
 



  $(document).ready(function(){

    update_cart()
   $('.add_to_cart').on('click', function(){
      id = $(this).attr('data-target')
      document.getElementById(id).style.display = 'none';
      document.getElementById(id+'plus').style.display = 'inline';
      document.getElementById(id+'minus').style.display = 'inline';
      document.getElementById('cartvalue'+id).style.display = 'inline';
      
     
     $.ajax({
      type:'GET',
      url:'{% url 'add_to_cart' %}',
      data:{'p_id':id},
      success:function(data){
        
       $('#cartvalue'+id).text(data);
       update_cart()
      }
            
     })
  
    })
   
     
  });


 


  function reduce_cart(id){
    $.ajax({
      type:'GET',
      url:'{% url 'reduce_cart' %}',
      data:{'p_id':id},
      success:function(data){
       
       $('#cartvalue'+id).text(data);
       if(data==0){

      document.getElementById(id).style.display = 'inline';
      document.getElementById(id+'plus').style.display = 'none';
      document.getElementById(id+'minus').style.display = 'none';
      document.getElementById('cartvalue'+id).style.display = 'none';
      
      

       }
       update_cart()
      }
            
     })
     
  }

  function increase_cart(id){


    $.ajax({
      type:'GET',
      url:'{% url 'increase_cart' %}',
      data:{'p_id':id},
      success:function(data){

      
       $('#cartvalue'+id).text(data);
       update_cart()
      }
            
     })
      }
function update_cart(){

$.ajax({
  type:'GET',
  url:'{% url 'update_cart' %}',
  success:function(data){
    console.log('data')
    console.log(data)
   $('#cart').text(data);
  }

})
}




 /* $(document).ready(function(){
    $('.add_to_cart').on('click', function(){
      id = $(this).attr('data-target')

    
     
     $.ajax({
      type:'GET',
      url:'{% url 'add_to_cart' %}',
      data:{'p_id':id},
      success:function(data){
        console.log(data)
        
       $('#cartvalue'+id).text(data);
      }
            
     })
     
    })
    
  });
*/
  
</script>

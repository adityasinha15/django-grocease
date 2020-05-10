<script>
  $(document).ready(function(){
    $('.add_to_cart').on('click', function(){
     p_id = $(this).attr('data-target')
     $.ajax({
      type:'GET',
      url:'{% url 'add_to_cart' %}',
      data:{'p_id':p_id},
      success:function(data){
        console.log('success')      }
     })
    })

  });

  function hideCartButton(id){
    document.getElementById(id).style.display = 'none';
    document.getElementById(id+'plus').style.display = 'inline';
    document.getElementById(id+'minus').style.display = 'inline';
    document.getElementById('cartvalue'+id).innerHTML = '<h1>one</h1>';
   
  }
</script>
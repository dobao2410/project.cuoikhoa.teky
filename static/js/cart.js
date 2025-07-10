(function($) {

    // var carts = {
    //     id,
    //     name,
    //     img,
    //     price,
    //     quantity
    // }
    // var carts = {
    //     // "product_name_1": {
    //     //     "id": 1,
    //     //     "name": "abc",
    //     // },
    //     // "product_name_2": {
    //     //     "id": 2,
    //     //     "name": "cba",
    //     // }
    // }
    // localStorage.setItem('carts', JSON.stringify(carts));

    // được bắt đầu khi web hoạt động

    $(document).ready(function() {
        let carts = JSON.parse(localStorage.getItem('carts')) || {};
        $(".number-shopping-cart").text(Object.keys(carts).length)

        $('#cart-modal').on('shown.bs.modal', function () {
            console.log("Modal đã mở");
            $('#btn-cart-modal').trigger('focus');
        });
        // Mở modal khi click
        $('.icon-cart').click(function (e) {
            e.preventDefault();
            const modal = new bootstrap.Modal(document.getElementById('cart-modal'));
            modal.show();
            const carts = JSON.parse(localStorage.getItem('carts')) || {};
            const $container = $("#cart-items-container");
            $container.empty(); // Xóa cũ

            if (Object.keys(carts).length === 0) {
                $container.html('<p>Giỏ hàng trống.</p>');
                return;
            }

            for (let id in carts) {
                const item = carts[id];
                const itemHtml = `
                    <div class="cart-item border p-2 mb-2 d-flex align-items-center">
                        <img src="${item.productImg}" alt="${item.productName}" style="width: 80px; height: 80px; object-fit: cover; margin-right: 10px;">
                        <div>
                            <h6 class="mb-1">${item.productName}</h6>
                            <p class="mb-0">Giá: ${Number(item.productPrice).toLocaleString('vi-VN')} đ</p>
                            <div class="btn-group btn-group-sm" role="group" aria-label="Small button group">
                                <p class="mb-0">Số lượng: </p>
                                <button type="button" class="btn btn-outline-primary">-</button>
                                <button type="button" class="btn btn-outline-primary">${item.quantity}</button>
                                <button type="button" class="btn btn-outline-primary">+</button>
                            </div>
                        </div>
                    </div>
                `;
                $container.append(itemHtml);
            }
        },);




    })


    $(".add-cart").click(function() {
        // debugger
        const productId = $("#product-id").val();
        const productName = $("#product-name").attr("data-product-name");
        const productImg = $("#product-img").attr("data-product-img");
        const productPrice = $("#product-price").attr("data-product-price");

        let carts = JSON.parse(localStorage.getItem('carts')) || {};
        if (!carts) {
            // Chưa có carts → tạo mới
            localStorage.setItem('carts', JSON.stringify({}));
        }
        // Tìm kiếm id có trong carts localstorage không
        var quantity = 1;
        if(carts[productId]) {
            quantity = carts[productId].quantity + 1;
        } 
        carts[productId] = {
            'id': productId,
            'productName': productName,
            'productImg': productImg,
            'productPrice': productPrice,
            'quantity': quantity
        }
        localStorage.setItem('carts', JSON.stringify(carts));
        // alert("Lưu sản phẩm thành công");
        toastr.success("Lưu thành công")
    });
    // modal




})(jQuery);
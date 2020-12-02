package com.example.brec;

import android.content.Context;
import android.text.Html;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.load.engine.DiskCacheStrategy;
import com.example.brec.model.Item;

import java.util.ArrayList;

public class BookAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

    private Context mContext;

    private ArrayList<Item> mBookInfoArrayList;

    public BookAdapter(Context context, ArrayList<Item> bookInfoArrayList) {
        mContext = context;
        mBookInfoArrayList = bookInfoArrayList;
    }

    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View v = inflater.inflate(R.layout.book_item, parent, false);
        return new BookViewHolder(v);
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, int position) {
        BookViewHolder bookViewHolder = (BookViewHolder) holder;

        Item item = mBookInfoArrayList.get(position);
        bookViewHolder.mbkTitle.setText(Html.fromHtml(item.getTitle()));
        bookViewHolder.mbkPubData.setText(item.getPubdate());
        bookViewHolder.mbkAuthor.setText(Html.fromHtml(item.getAuthor()));
        bookViewHolder.mbkPublisher.setText(Html.fromHtml(item.getPublisher()));
        bookViewHolder.mbkPrice.setText(Html.fromHtml(item.getPrice()));

        Glide.with(mContext)
                .load(item.getImage())
                .diskCacheStrategy(DiskCacheStrategy.ALL)
                .into(bookViewHolder.getImage());
    }

    @Override
    public int getItemCount() {
        return mBookInfoArrayList.size();
    }

    public void clearItems() {
        mBookInfoArrayList.clear();
        notifyDataSetChanged();
    }

    public void clearAndAddItems(ArrayList<Item> items) {
        mBookInfoArrayList.clear();
        mBookInfoArrayList.addAll(items);
        notifyDataSetChanged();
    }

    public static class BookViewHolder extends RecyclerView.ViewHolder {

        private ImageView mbkImage;
        private TextView mbkTitle;
        private TextView mbkPubData;
        private TextView mbkAuthor;
        private TextView mbkPublisher;
        private TextView mbkPrice;

        BookViewHolder(View view) {
            super(view);
            mbkImage = view.findViewById(R.id.iv_poster);
            mbkTitle = view.findViewById(R.id.bk_title);
            mbkPubData = view.findViewById(R.id.bk_pub_data);
            mbkAuthor = view.findViewById(R.id.bk_author);
            mbkPublisher = view.findViewById(R.id.bk_publisher);
            mbkPrice = view.findViewById(R.id.bk_price);
        }

        public ImageView getImage() {
            return mbkImage;
        }

    }
}

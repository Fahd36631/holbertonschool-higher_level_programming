--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked --
SELECT t.title , ts.genre_id FROM tv_shows t , tv_show_genres ts
WHERE t.id = ts.show_id
ORDER BY t.title ASC , ts.genre_id ASC;
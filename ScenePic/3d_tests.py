import argparse
import numpy as np
import scenepic as sp

Name = "getting_started"
Title = "Getting Started"


def build_scene() -> sp.Scene:
    # when we build a ScenePic we are essentially building a web
    # page, and the ScenePic will automatically populate parts of
    # that webpage.

    # the scene object acts as the root of the entire ScenePic environment
    scene = sp.Scene()

    sp.Shading(bg_color=sp.Colors.Gray, directional_light_color=np.array([0, 0 ,0]))

    # you can use it to create one or more canvases to display 3D or 2D
    # objects. Canvas objects display Frames. For a static ScenePic, there
    # will only be a single Frame, but you can use multiple frames to create
    # an animation or to display a range of visualizations in the same visual
    # space. We will create one 3D canvas to display the full scene, and then
    # some 2D canvases which will show projections of the scene.
    main = scene.create_canvas_3d(width=600, height=600)
    # projx = scene.create_canvas_2d("projx", width=200, height=200)
    # projy = scene.create_canvas_2d("projy", width=200, height=200)
    # projz = scene.create_canvas_2d("projz", width=200, height=200)

    # the scene object is also used to create Mesh objects that will be added
    # to frames. We are going to create an animation of some spheres orbiting
    # a fixed cube, so let's create a default unit cube to start.
    # cube = scene.create_mesh("cube")

    # cube2 = scene.create_mesh("cube2")
    # cube2.add_cube(color=sp.Colors.Purple)

    cube_size = 0.1
    multicubes = []
    for i in range(-10, 11):
        for j in range(-10, 11):
            # multicube = scene.create_mesh(f"{i}_{j}")
            # multicube.add_cube(color=sp.Colors.White)
            # multicube.apply_transform(sp.Transforms.Translate(np.array([i * cube_size, j * cube_size, 0])))
            # multicube.apply_transform(sp.Transforms.Scale(np.array([1, 1, np.random.random_sample()])))
            # multicubes.append(multicube)

            height = np.random.random_sample() * 0.1
            max_height = 0.1
            cs = cube_size/2
            cube_verts = np.array([[-cs, -cs, 0.0], [+cs, -cs, 0.0], [-cs, +cs, 0.0], [+cs, +cs, 0.0], [-cs, -cs, height], [+cs, -cs, height], [-cs, +cs, height], [+cs, +cs, height]])
            cube_tris = np.array([[0, 2, 3], [0, 3, 1], [1, 3, 7], [1, 7, 5], [4, 5, 7], [4, 7, 6], [4, 6, 2], [4, 2, 0], [2, 6, 7], [2, 7, 3], [4, 0, 1], [4, 1, 5]])
            multicube = scene.create_mesh(f"{i}_{j}", shared_color = sp.Color(0.2, (1.0/max_height * height)/2, (1.0/max_height * height)/2))
            multicube.add_mesh_without_normals(cube_verts, cube_tris, transform = sp.Transforms.Translate([-1.0, 0.0, 0.0])) # Add non-subdivided cube
            multicube.apply_transform(sp.Transforms.Translate(np.array([i * cube_size, j * cube_size, 0])))
            multicubes.append(multicube)
            # mesh3.add_mesh_without_normals(cube_verts_a, cube_tris_a)
            # mesh3.add_mesh_without_normals(cube_verts_b, cube_tris_b, transform = sp.Transforms.Translate([+1.0, 0.0, 0.0]))


    # the Mesh object has a variety of methods for adding primitive objects
    # or loading arbitrary mesh geometry. In this example, we will just
    # be using primitives, but the python tutorial shows all the various
    # methods for adding geometry to a mesh.
    # cube.add_cube(color=sp.Colors.White)

    # let's create our spheres as well, using some different colors
    # sphere_names = ["red", "green", "blue"]
    # sphere_colors = [sp.Colors.Red, sp.Colors.Green, sp.Colors.Blue]
    # spheres = []
    # for name, color in zip(sphere_names, sphere_colors):
    #     # by placing each sphere on a different layer, we can toggle them on and off
    #     sphere = scene.create_mesh("{}_sphere".format(name), layer_id=name)
    #     sphere.add_sphere(color=color, transform=sp.Transforms.scale(0.5))
    #     spheres.append(sphere)

    # now we will iteratively create each frame of the animation.
    for i in range(180):
        # first we create a frame object. This will be used to populate
        # the 3D canvas.
        main_frame = main.create_frame()

        # Now that we have a frame, we can add the cube mesh to the frame
        # main_frame.add_mesh(cube)
        # main_frame.add_mesh(cube2, transform = sp.Transforms.scale([1, 1, 5]))

        for multicube in multicubes:
            main_frame.add_mesh(multicube)

        # Next, we add the spheres. ScenePic has a variety of useful tools
        # for operating on 3D data. Some of the most useful enable us to
        # create transforms to move meshes around. Let's create the
        # transforms for our three rotating spheres and add them to the frame.
        # NB The Python interface uses numpy for matrices and vectors.
        # positions = np.concatenate([np.eye(3, dtype=np.float32) * 1.3,
        #                             np.ones((3, 1), dtype=np.float32)], axis=-1)
        # inc = 2 * np.pi / 180
        # positions[0] = sp.Transforms.RotationAboutYAxis(inc * i) @ positions[0].T
        # positions[1] = sp.Transforms.RotationAboutZAxis(2 * inc * i) @ positions[1].T
        # positions[2] = sp.Transforms.RotationAboutXAxis(3 * inc * i) @ positions[2].T
        # positions = positions[:, :3]
        # for sphere, position in zip(spheres, positions):
        #     transform = sp.Transforms.translate(position)
        #     main_frame.add_mesh(sphere, transform=transform)

        # now we'll populate our projections
        # for j, proj in enumerate([projx, projy, projz]):
        #     proj_frame = proj.create_frame()

        #     # 2D frames work in pixels (as oppose to world units) so we need
        #     # to convert positions to pixels.
        #     proj_frame.add_rectangle(75, 75, 50, 50, fill_color=sp.Colors.White)
        #     points = np.roll(positions, j, axis=1)[:, 1:]
        #     points[:, 1] *= -1
        #     points = points * 50 + 100

        #     for point, color in zip(points, sphere_colors):
        #         proj_frame.add_circle(point[0], point[1], 12.5, fill_color=color)

        #     # let's add some label text
        #     proj_frame.add_text(proj.canvas_id, 10, 190, size_in_pixels=16)

    # this will make user interactions happen to all canvases simultaneously
    # scene.link_canvas_events(main, projx, projy, projz)

    # ScenePic provides some useful layout controls by exposing CSS grid commands
    scene.grid(width="800px", grid_template_rows="200px 200px 200px", grid_template_columns="600px 200px")
    scene.place(main.canvas_id, "1 / span 3", "1")
    # scene.place(projx.canvas_id, "1", "2")
    # scene.place(projy.canvas_id, "2", "2")
    # scene.place(projz.canvas_id, "3", "2")
    return scene


def _parse_args():
    parser = argparse.ArgumentParser(Title)
    parser.add_argument("--script", action="store_true",
                        help="Whether to save the scenepic as a JS file")
    return parser.parse_args()


def _main():
    args = _parse_args()
    scene = build_scene()
    # The scene is complete, so we write it to a standalone file.
    if args.script:
        # If you have an existing HTML page you want to add a scenepic
        # to, then you can save the scenepic as a self-contained
        # Javascript file.
        scene.save_as_script("{}.js".format(Name), standalone=True)
    else:
        # However, ScenePic will also create a basic HTML wrapper
        # and embed the Javascript into the file directly so you
        # have a single file containing everything.
        scene.save_as_html("{}.html".format(Name), title=Title)


if __name__ == "__main__":
    _main()

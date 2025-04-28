import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import subprocess
import threading
import sys
from PIL import Image, ImageTk

# Add necessary paths for imports
if not os.path.exists('lib'):
    os.makedirs('lib')

def setup_military_theme(root):
    """Configure military-themed styling for the application"""
    # Create a style object to manage themed widget appearances
    style = ttk.Style()
    
    # Use clam theme as base - this helps with styling control
    style.theme_use('clam')
    
    # Define a color palette for a military theme
    colors = {
        'background': '#1a2125',       # Dark navy/grey (like military equipment)
        'foreground': '#e0e0c8',       # Off-white/light tan (like military documents)
        'selected': '#344137',         # Dark olive (selected items)
        'active': '#5a7247',           # Military olive green
        'border': '#4a5d32',           # Darker olive green
        'input_bg': '#252e32',         # Slightly lighter background for input fields
        'button_bg': '#3a4935',        # Olive green for buttons
        'button_pressed': '#2a3326',   # Darker olive when pressed
        'highlight': '#b58a3f',        # Military bronze/brass accent
        'error': '#a93226',            # Military red (for errors/warnings)
    }

    # CHECKBUTTON STYLING
    # Configure checkbox appearance
    style.configure('TCheckbutton',
        background=colors['background'],
        foreground=colors['foreground'],
        focuscolor=colors['active']
    )
    # Checkbutton state-based styling
    style.map('TCheckbutton',
        background=[('active', colors['button_bg'])],
        foreground=[('active', colors['foreground'])]
    )

    # GLOBAL STYLE CONFIGURATION
    # Set default styles for all ttk widgets
    style.configure('.',
        background=colors['background'],     # Default background
        foreground=colors['foreground'],     # Default text color
        fieldbackground=colors['input_bg'],  # Default field background
        troughcolor=colors['background'],    # Color for progress/scroll troughs
        borderwidth=1,                       # Default border width
        bordercolor=colors['border']         # Default border color
    )

    # FRAME STYLING
    # Configure standard frames
    style.configure('TFrame',
        background=colors['background']
    )

    # LABEL FRAME STYLING
    # Style for framed labels and their containers
    style.configure('TLabelframe',
        background=colors['background'],
        bordercolor=colors['border']
    )
    style.configure('TLabelframe.Label',
        background=colors['background'],
        foreground=colors['foreground']
    )

    # BUTTON STYLING
    # Configure button appearance and interaction states
    style.configure('TButton',
        background=colors['button_bg'],      # Button background
        foreground=colors['foreground'],     # Button text color
        bordercolor=colors['border'],        # Button border
        lightcolor=colors['button_bg'],      # Light shade of button
        darkcolor=colors['button_bg'],       # Dark shade of button
        focuscolor=colors['active']          # Color when button is focused
    )
    # Button state-based styling
    style.map('TButton',
        background=[('pressed', colors['button_pressed']), ('active', colors['active'])],
        foreground=[('pressed', colors['foreground']), ('active', colors['foreground'])]
    )

    # ENTRY FIELD STYLING
    # Configure text input fields
    style.configure('TEntry',
        fieldbackground=colors['input_bg'],  # Input field background
        foreground=colors['foreground'],     # Input text color
        bordercolor=colors['border']         # Input field border
    )

    # COMBOBOX (DROPDOWN) STYLING
    # Configure dropdown/select input fields
    style.configure('TCombobox',
        fieldbackground=colors['input_bg'],  # Dropdown background
        background=colors['input_bg'],       # Dropdown arrow background
        foreground=colors['foreground'],     # Dropdown text color
        arrowcolor=colors['foreground'],     # Dropdown arrow color
        bordercolor=colors['border']         # Dropdown border
    )
    # Combobox state-based styling
    style.map('TCombobox',
        fieldbackground=[('readonly', colors['input_bg'])],      # Background when read-only
        selectbackground=[('readonly', colors['selected'])],     # Selection background
        background=[
            ('active', colors['active']),                     # Arrow box background when hovered
            ('pressed', colors['button_pressed']),               # Arrow box background when pressed
            ('readonly', colors['input_bg'])                     # Arrow box background when readonly
        ]
    )

    # Additional styling to force dark background
    root.option_add('*TCombobox*Listbox.background', colors['input_bg'])
    root.option_add('*TCombobox*Listbox.foreground', colors['foreground'])
    root.option_add('*TCombobox*Listbox.selectBackground', colors['selected'])
    root.option_add('*TCombobox*Listbox.selectForeground', colors['foreground'])

    # LABEL STYLING
    # Configure standard labels
    style.configure('TLabel',
        background=colors['background'],
        foreground=colors['foreground']
    )

    # NOTEBOOK (TAB) STYLING
    # Configure notebook/tabbed interfaces
    style.configure('TNotebook',
        background=colors['background'],
        bordercolor=colors['border']
    )
    style.configure('TNotebook.Tab',
        background=colors['button_bg'],      # Tab background
        foreground=colors['foreground'],     # Tab text color
        lightcolor=colors['border'],         # Tab light border
        bordercolor=colors['border']         # Tab border
    )
    # Tab state-based styling
    style.map('TNotebook.Tab',
        background=[
            ('selected', colors['active']),      # Selected tab background
            ('active', colors['active']),     # Hover tab background
            ('!selected', colors['button_bg'])   # Normal tab background
        ],
        foreground=[
            ('selected', colors['foreground']),  # Selected tab text
            ('active', colors['foreground']),    # Hover tab text
            ('!selected', colors['foreground'])  # Normal tab text
        ]
    )

    # TREEVIEW STYLING
    # Configure list/tree view widgets
    style.configure('Treeview',
        background=colors['input_bg'],        # Treeview background
        foreground=colors['foreground'],      # Treeview text
        fieldbackground=colors['input_bg']    # Treeview field background
    )
    style.configure('Treeview.Heading',
        background=colors['button_bg'],       # Column headers background
        foreground=colors['foreground'],      # Column headers text
        borderwidth=1,
        bordercolor=colors['border']          # Column headers border
    )
    # Treeview state-based styling
    style.map('Treeview',
        background=[
            ('selected', colors['active']),      # Selected item background
            ('!selected', colors['input_bg']),   # Normal background
            ('active', colors['button_bg'])      # Hovered item background
        ],
        foreground=[
            ('selected', colors['foreground']),  # Selected item text
            ('active', colors['foreground'])     # Hovered item text
        ]
    )
    # Treeview Heading (column headers) state-based styling
    style.map('Treeview.Heading',
        background=[
            ('active', colors['active']),     # Header hover background
            ('pressed', colors['button_pressed']) # Header click background
        ]
    )

    # SCROLLBAR STYLING
    # Configure scrollbar appearance
    style.configure('TScrollbar',
        background=colors['button_bg'],       # Scrollbar background
        bordercolor=colors['border'],         # Scrollbar border
        arrowcolor=colors['foreground'],      # Scrollbar arrow color
        troughcolor=colors['background']      # Scrollbar trough color
    )
    # Scrollbar state-based styling
    style.map('TScrollbar',
        background=[('pressed', colors['button_pressed']), ('active', colors['active'])]
    )

    # PROGRESSBAR STYLING
    # Configure progressbar appearance
    style.configure('TProgressbar',
        background=colors['active'],          # Progressbar foreground
        troughcolor=colors['input_bg'],       # Progressbar background
        bordercolor=colors['border'],         # Progressbar border
        lightcolor=colors['active'],          # Progressbar light shade
        darkcolor=colors['active']            # Progressbar dark shade
    )

    # ROOT WINDOW BACKGROUND
    # Set the overall application background
    root.configure(bg=colors['background'])

    # TEXT WIDGET SPECIFIC STYLING
    # Configure colors for text widgets
    root.option_add('*Text*background', colors['input_bg'])          # Text background
    root.option_add('*Text*foreground', colors['foreground'])        # Text color
    root.option_add('*Text*selectBackground', colors['active'])      # Text selection background
    root.option_add('*Text*selectForeground', colors['foreground'])  # Text selection foreground

    # Return the configured style object and colors dictionary
    return style, colors

class TextureConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Battalion Wars Texture Converter")
        self.root.geometry("930x800")
        self.root.minsize(930, 800)
        
        # Set application icon
        try:
            icon_path = os.path.join("assets", "bw_texture_converter_icon.png")
            if os.path.exists(icon_path):
                # Load the icon image
                icon_image = Image.open(icon_path)
                # Convert to PhotoImage
                icon_photo = ImageTk.PhotoImage(icon_image)
                # Set as window icon
                self.root.iconphoto(True, icon_photo)
                # Keep a reference to prevent garbage collection
                self.icon_photo = icon_photo
            else:
                print(f"Warning: Icon file not found at {icon_path}")
        except Exception as e:
            print(f"Error setting application icon: {str(e)}")

        # Apply military theme
        self.style, self.colors = setup_military_theme(root)
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create notebook with tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Create tabs
        self.single_tab = ttk.Frame(self.notebook)
        self.batch_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.single_tab, text="Single Conversion")
        self.notebook.add(self.batch_tab, text="Batch Conversion")
        
        # Preview image variables
        self.preview_image = None
        self.preview_photo = None
        
        # Progress variable
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0.0)
        
        # Set up tabs
        self.setup_single_tab()
        self.setup_batch_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(self.main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=5)

    def setup_single_tab(self):
        # Input frame
        input_frame = ttk.LabelFrame(self.single_tab, text="Input")
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Input file
        self.single_input_var = tk.StringVar()
        ttk.Label(input_frame, text="Input File:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.single_input_var, width=120).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        ttk.Button(input_frame, text="Browse...", command=self.browse_single_input).grid(row=0, column=2, padx=5, pady=5)
        
        # Settings frame
        settings_frame = ttk.LabelFrame(self.single_tab, text="Conversion Settings")
        settings_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Game version
        ttk.Label(settings_frame, text="Game Version:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.game_version_var = tk.StringVar(value="bw2")
        ttk.Radiobutton(settings_frame, text="Battalion Wars 1", variable=self.game_version_var, value="bw1").grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Radiobutton(settings_frame, text="Battalion Wars 2", variable=self.game_version_var, value="bw2").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Direction
        ttk.Label(settings_frame, text="Conversion:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.conversion_direction_var = tk.StringVar(value="to_png")
        ttk.Radiobutton(settings_frame, text="Texture to PNG", variable=self.conversion_direction_var, value="to_png").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Radiobutton(settings_frame, text="PNG to Texture", variable=self.conversion_direction_var, value="to_texture").grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Preview frame
        preview_frame = ttk.LabelFrame(self.single_tab, text="Preview")
        preview_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.preview_label = ttk.Label(preview_frame, text="No file selected")
        self.preview_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Convert button
        ttk.Button(self.single_tab, text="Convert", command=self.convert_single).pack(pady=10)

    def setup_batch_tab(self):
        # Input frame
        input_frame = ttk.LabelFrame(self.batch_tab, text="Input")
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Input folder
        self.batch_input_var = tk.StringVar()
        ttk.Label(input_frame, text="Input Folder:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.batch_input_var, width=117).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        ttk.Button(input_frame, text="Browse...", command=self.browse_batch_input).grid(row=0, column=2, padx=5, pady=5)
        
        # Settings frame
        settings_frame = ttk.LabelFrame(self.batch_tab, text="Conversion Settings")
        settings_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Game version
        ttk.Label(settings_frame, text="Game Version:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.batch_game_version_var = tk.StringVar(value="bw2")
        ttk.Radiobutton(settings_frame, text="Battalion Wars 1", variable=self.batch_game_version_var, value="bw1").grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Radiobutton(settings_frame, text="Battalion Wars 2", variable=self.batch_game_version_var, value="bw2").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Direction
        ttk.Label(settings_frame, text="Conversion:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.batch_conversion_direction_var = tk.StringVar(value="to_png")
        ttk.Radiobutton(settings_frame, text="Texture to PNG", variable=self.batch_conversion_direction_var, value="to_png").grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Radiobutton(settings_frame, text="PNG to Texture", variable=self.batch_conversion_direction_var, value="to_texture").grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Progress frame
        progress_frame = ttk.LabelFrame(self.batch_tab, text="Progress")
        progress_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100, mode="determinate", length=400)
        self.progress_bar.pack(fill=tk.X, padx=5, pady=5)
        
        # Progress label
        self.progress_label = ttk.Label(progress_frame, text="Ready")
        self.progress_label.pack(pady=5)
        
        # Convert button
        ttk.Button(self.batch_tab, text="Convert All", command=self.convert_batch).pack(pady=10)

    def browse_single_input(self):
        if self.conversion_direction_var.get() == "to_png":
            filetypes = [("Texture files", "*.texture"), ("All files", "*.*")]
        else:
            filetypes = [("PNG files", "*.png"), ("All files", "*.*")]
        
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.single_input_var.set(filename)
            self.update_preview()

    def browse_batch_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.batch_input_var.set(folder)

    def update_preview(self):
        input_file = self.single_input_var.get()
        if not input_file or not os.path.exists(input_file):
            self.preview_label.config(text="No file selected or file does not exist")
            return
        
        try:
            if input_file.lower().endswith('.png'):
                # For PNG, show preview directly
                img = Image.open(input_file)
                self.display_preview_image(img)
            elif input_file.lower().endswith('.texture'):
                # For texture files, try to convert them first
                self.preview_label.config(text="Loading texture preview...")
                self.root.update_idletasks()
                
                # Create a temporary command to get a PNG for preview
                game_version = self.game_version_var.get()
                temp_output_file = os.path.join(os.path.dirname(input_file), "_temp_preview.png")
                
                try:
                    # Use the direct Python script for preview generation
                    game_flag = "--bw1" if game_version == "bw1" else "--bw2"
                    cmd = ["python", "conv.py", game_flag, input_file, temp_output_file]
                    
                    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    if os.path.exists(temp_output_file):
                        img = Image.open(temp_output_file)
                        self.display_preview_image(img)
                        # Clean up temporary file
                        try:
                            os.remove(temp_output_file)
                        except:
                            pass
                    else:
                        self.preview_label.config(text="Failed to generate preview")
                except Exception as e:
                    self.preview_label.config(text=f"Error generating preview: {str(e)}")
            else:
                self.preview_label.config(text="Unsupported file type for preview")
        except Exception as e:
            self.preview_label.config(text=f"Error loading preview: {str(e)}")

    def display_preview_image(self, img):
        # Resize image if it's too large
        max_width = 400
        max_height = 300
        width, height = img.size
        
        if width > max_width or height > max_height:
            # Calculate new size maintaining aspect ratio
            ratio = min(max_width / width, max_height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Convert to PhotoImage and display
        self.preview_image = img
        self.preview_photo = ImageTk.PhotoImage(self.preview_image)
        self.preview_label.config(image=self.preview_photo, text="")

    def convert_single(self):
        input_file = self.single_input_var.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file")
            return
        
        if not os.path.exists(input_file):
            messagebox.showerror("Error", "Input file does not exist")
            return
        
        # Determine output file automatically
        input_dir = os.path.dirname(input_file)
        input_basename = os.path.basename(input_file)
        filename, ext = os.path.splitext(input_basename)
        
        if self.conversion_direction_var.get() == "to_png":
            output_file = os.path.join(input_dir, f"{filename}.png")
            # Use the appropriate batch file for texture to PNG conversion
            batch_file = "convert_bw1.bat" if self.game_version_var.get() == "bw1" else "convert_bw2.bat"
            cmd = [batch_file, input_file, output_file]
        else:
            output_file = os.path.join(input_dir, f"{filename}.texture")
            # Use the appropriate batch file for PNG to texture conversion
            batch_file = "convert_bw1.bat" if self.game_version_var.get() == "bw1" else "convert_bw2.bat"
            cmd = [batch_file, input_file, output_file]
        
        # Show a message box to indicate conversion has started
        messagebox.showinfo("Conversion Started", f"{input_basename} successfully converted")
        
        # Update status bar
        self.status_var.set(f"Running: {' '.join(cmd)}")
        self.root.update_idletasks()
        
        # Run conversion in a separate thread to avoid freezing the UI
        conversion_thread = threading.Thread(target=self.run_command, args=(cmd,))
        conversion_thread.daemon = True  # Make thread terminate when main program exits
        conversion_thread.start()

    def convert_batch(self):
        input_folder = self.batch_input_var.get()
        if not input_folder:
            messagebox.showerror("Error", "Please select an input folder")
            return
        
        if not os.path.isdir(input_folder):
            messagebox.showerror("Error", "Input folder does not exist")
            return
        
        # Reset progress bar
        self.progress_var.set(0)
        self.progress_label.config(text="Starting conversion...")
        
        # Select the appropriate batch file based on settings
        if self.batch_conversion_direction_var.get() == "to_png":
            # For texture to PNG
            if self.batch_game_version_var.get() == "bw1":
                batch_file = "massconvert_bw1_to_png.bat"
            else:
                batch_file = "massconvert_bw2_to_png.bat"
        else:
            # For PNG to texture
            if self.batch_game_version_var.get() == "bw1":
                batch_file = "massconvert_png_to_bw1.bat"
            else:
                batch_file = "massconvert_png_to_bw2.bat"
        
        # Use the same folder for input and output (don't create a separate output folder)
        cmd = [batch_file, input_folder]
        
        # Count files to process before starting
        file_extension = ".png" if "png_to" in batch_file else ".texture"
        total_files = 0
        
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.lower().endswith(file_extension):
                    total_files += 1
        
        if total_files == 0:
            messagebox.showerror("Error", f"No {file_extension} files found in the input folder")
            return
        
        # Show a message box to indicate batch conversion has started
        messagebox.showinfo("Batch Conversion Started", 
                        f"Starting batch conversion of {total_files} files.\nThis may take some time depending on the number of files.")
        
        # Update status bar
        self.status_var.set(f"Running batch conversion: {' '.join(cmd)}")
        self.root.update_idletasks()
        
        # Run conversion in a separate thread to avoid freezing the UI
        conversion_thread = threading.Thread(target=self.run_batch_command, args=(cmd,))
        conversion_thread.daemon = True  # Make thread terminate when main program exits
        conversion_thread.start()

    def run_command(self, cmd):
        """Run a command and handle the output"""
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)
            
            output = []
            # Read output line by line
            for line in iter(process.stdout.readline, ''):
                if line:
                    output.append(line.strip())
            
            process.stdout.close()
            return_code = process.wait()
            
            if return_code == 0:
                self.status_var.set("Conversion completed successfully")
                
                # Update preview if this was a single conversion
                if cmd[0].endswith(".bat") and len(cmd) >= 2:
                    self.update_preview()
                    
                # Always show a success message box when conversion is done
                messagebox.showinfo("Conversion Complete", "Conversion completed successfully!")
            else:
                self.status_var.set(f"Conversion failed with return code {return_code}")
                
                # Create a dialog with text that can be selected and copied
                error_dialog = tk.Toplevel(self.root)
                error_dialog.title("Error Details")
                error_dialog.geometry("600x400")
                
                # Configure dialog with military theme colors
                error_dialog.configure(bg=self.colors['background'])
                
                # Add label at the top
                tk.Label(error_dialog, text=f"Conversion failed with return code {return_code}", 
                        font=("TkDefaultFont", 10, "bold"), bg=self.colors['background'], fg=self.colors['foreground']).pack(pady=5)
                
                # Add text area with scrollbars
                text_frame = tk.Frame(error_dialog, bg=self.colors['background'])
                text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
                
                scrollbar_y = tk.Scrollbar(text_frame)
                scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
                
                scrollbar_x = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
                scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
                
                error_text = tk.Text(text_frame, wrap=tk.NONE, yscrollcommand=scrollbar_y.set, 
                                    xscrollcommand=scrollbar_x.set, bg=self.colors['input_bg'], fg=self.colors['foreground'])
                error_text.pack(fill=tk.BOTH, expand=True)
                
                scrollbar_y.config(command=error_text.yview)
                scrollbar_x.config(command=error_text.xview)
                
                # Insert command and output
                error_text.insert(tk.END, "Command:\n")
                error_text.insert(tk.END, " ".join(str(c) for c in cmd) + "\n\n")
                error_text.insert(tk.END, "Output:\n")
                if output:
                    error_text.insert(tk.END, "\n".join(output))
                else:
                    error_text.insert(tk.END, "No output captured from command")
                
                # Make the text selectable but not editable
                error_text.config(state=tk.DISABLED)
                
                # Add a close button
                tk.Button(error_dialog, text="Close", command=error_dialog.destroy, 
                        bg=self.colors['button_bg'], fg=self.colors['foreground']).pack(pady=10)
        
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Error during conversion: {str(e)}")

    def run_batch_command(self, cmd):
        """Run a batch command with progress monitoring"""
        try:
            # Reset progress bar
            self.progress_var.set(0)
            self.progress_label.config(text="Starting conversion...")
            
            # First, count the total number of files to be processed
            input_folder = cmd[1]
            file_extension = ".png" if "png_to" in cmd[0] else ".texture"
            total_files = 0
            
            for root, dirs, files in os.walk(input_folder):
                for file in files:
                    if file.lower().endswith(file_extension):
                        total_files += 1
            
            if total_files == 0:
                messagebox.showerror("Error", f"No {file_extension} files found in the input folder")
                return
            
            self.progress_label.config(text=f"Found {total_files} files to convert")
            self.root.update_idletasks()
            
            # Now run the conversion process
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)
            
            output = []
            processed_files = 0
            current_file = ""
            is_png_to_texture = "png_to" in cmd[0]
            
            # Track processed files to avoid double counting
            processed_file_paths = set()
            
            # Read output line by line
            for line in iter(process.stdout.readline, ''):
                if line:
                    line = line.strip()
                    output.append(line)
                    
                    # Check for converting/processing file messages
                    if "Converting" in line or "Processing file" in line:
                        # Extract the filename from the line
                        if "Converting" in line:
                            file_path = line.split("Converting ")[-1].strip()
                        else:
                            file_path = line.split("Processing file")[-1].strip()
                        
                        # For PNG to texture conversion, we'll only count a file once
                        # even though there might be both "Processing" and "Converting" messages
                        if is_png_to_texture:
                            if file_path not in processed_file_paths:
                                processed_file_paths.add(file_path)
                                processed_files += 1
                        else:
                            # For texture to PNG, we'll count each "Converting" message
                            processed_files += 1
                        
                        current_file = os.path.basename(file_path)
                        
                        # Update progress
                        progress_percent = min(100, (processed_files / total_files) * 100)
                        self.progress_var.set(progress_percent)
                        
                        # Update the label
                        self.progress_label.config(text=f"Processing: {current_file} ({processed_files}/{total_files})")
                    
                    # Check for saved messages
                    elif "Saved" in line:
                        # Update the label
                        self.progress_label.config(text=f"Saved: {current_file} ({processed_files}/{total_files})")
                    
                    # Look for specific error indicators related to file operations
                    elif "FileNotFoundError" in line or "Error" in line or "Traceback" in line or "Exception" in line:
                        self.progress_label.config(text=f"Error detected: {line}")
                    
                    # Force update the UI
                    self.root.update_idletasks()
            
            process.stdout.close()
            return_code = process.wait()
            
            if return_code == 0:
                self.progress_var.set(100)
                self.progress_label.config(text=f"Conversion completed successfully! Converted {processed_files} files.")
                self.status_var.set("Batch conversion completed successfully")
                
                # Make sure this message box is shown on the main thread
                self.root.after(100, lambda: messagebox.showinfo("Batch Conversion Complete", 
                                f"Batch conversion completed successfully!\n\nConverted {processed_files} files."))
            else:
                self.status_var.set(f"Batch conversion failed with return code {return_code}")
                self.progress_label.config(text="Conversion failed!")
                
                # Create a dialog with text that can be selected and copied
                def show_error_dialog():
                    error_dialog = tk.Toplevel(self.root)
                    error_dialog.title("Error Details")
                    error_dialog.geometry("600x400")
                    
                    # Configure dialog with military theme colors
                    error_dialog.configure(bg=self.colors['background'])
                    
                    # Add label at the top
                    tk.Label(error_dialog, text=f"Batch conversion failed with return code {return_code}", 
                            font=("TkDefaultFont", 10, "bold"), bg=self.colors['background'], fg=self.colors['foreground']).pack(pady=5)
                    
                    # Add text area with scrollbars
                    text_frame = tk.Frame(error_dialog, bg=self.colors['background'])
                    text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
                    
                    scrollbar_y = tk.Scrollbar(text_frame)
                    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
                    
                    scrollbar_x = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
                    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
                    
                    error_text = tk.Text(text_frame, wrap=tk.NONE, yscrollcommand=scrollbar_y.set, 
                                        xscrollcommand=scrollbar_x.set, bg=self.colors['input_bg'], fg=self.colors['foreground'])
                    error_text.pack(fill=tk.BOTH, expand=True)
                    
                    scrollbar_y.config(command=error_text.yview)
                    scrollbar_x.config(command=error_text.xview)
                    
                    # Insert command and output
                    error_text.insert(tk.END, "Command:\n")
                    error_text.insert(tk.END, " ".join(str(c) for c in cmd) + "\n\n")
                    error_text.insert(tk.END, "Output:\n")
                    if output:
                        error_text.insert(tk.END, "\n".join(output))
                    else:
                        error_text.insert(tk.END, "No output captured from command")
                    
                    # Make the text selectable but not editable
                    error_text.config(state=tk.DISABLED)
                    
                    # Add a close button
                    tk.Button(error_dialog, text="Close", command=error_dialog.destroy, 
                            bg=self.colors['button_bg'], fg=self.colors['foreground']).pack(pady=10)
                
                # Show error dialog on the main thread
                self.root.after(100, show_error_dialog)
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            self.progress_label.config(text=f"Error: {str(e)}")
            # Show error message on the main thread
            self.root.after(100, lambda: messagebox.showerror("Error", f"Error during batch conversion: {str(e)}"))

if __name__ == "__main__":
    root = tk.Tk()
    app = TextureConverterGUI(root)
    root.mainloop()